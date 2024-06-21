"""Data loading and writing module
"""

import logging
import os
import struct
import xml.etree.ElementTree as ET

# Import libraries necessary for the analysis
from io import StringIO
from typing import Literal, Optional

import pandas as pd
import pyodbc
import sqlalchemy
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.storage.filedatalake import DataLakeServiceClient

logger = logging.getLogger(__name__)


class BlobStorage:
    """BlobStorage object to connect with Azure storage account"""

    def __init__(self, storage_account_name: str, blob_container_name: str):
        try:
            default_credential = DefaultAzureCredential(
                exclude_environment_credential=True,
                exclude_managed_identity_credential=True,
                exclude_visual_studio_code_credential=False,
                exclude_shared_token_cache_credential=True,
                exclude_interactive_browser_credential=True,
            )
            self.service_client = DataLakeServiceClient(
                account_url="{}://{}.dfs.core.windows.net".format(
                    "https", storage_account_name
                ),
                credential=default_credential,
            )
            self.file_system_client = self.service_client.get_file_system_client(
                file_system=blob_container_name
            )
            self.blob_service_client = BlobServiceClient(
                account_url="{}://{}.blob.core.windows.net".format(
                    "https", storage_account_name
                ),
                credential=default_credential,
            )

        except Exception as e:
            print("Error in initialize_storage_account: ", e)

    # create function to access directory content
    def list_directory_contents(self, directory: str) -> list[str]:
        """List directory content of your Azure storage account

        Args:
            directory (str): path to the directory

        Returns:
            list[str]: A list of all the files in the directory
        """
        try:
            paths = self.file_system_client.get_paths(path=directory)

            directory_content = []

            for path in paths:
                directory_content.append(path.name)

            return directory_content

        except Exception as e:
            print("Error in list_directory_contents: ", e)

    # Function to download a csv file from Azure
    def download_csv_file_from_directory(
        self, file_path: str, separator: str = ";"
    ) -> pd.DataFrame:  # the name of the file path (e.g., folder/file_name.csv)
        """Download csv files from a specific location within the blob container

        Args:
            file_path (str): the path to the flat file you want to download (e.g., folder/file_name.csv)
            separator (str, optional): the separator used in the csv. Default to ; (semicolon)

        Raises:
            ValueError: file_name must end with .csv

        Returns:
            pd.DataFrame: The pandas DataFrame based on the csv file
        """
        if not file_path.endswith(".csv"):
            raise ValueError("file_name must end with .csv")
        try:
            file_client = self.file_system_client.get_file_client(file_path=file_path)
            fileBytesObject = file_client.download_file().readall()
            s = str(fileBytesObject, "utf-8")
            data = StringIO(s)
            df = pd.read_csv(data, sep=separator)
            return df
        except Exception as e:
            print(e)

    # Function to download a .xlsx file from Azure
    def download_xlsx_file_from_directory(
        self, file_path: str, sheet_name: str = None
    ) -> pd.DataFrame:  # the name of the file path (e.g., folder/file_name.xlsx)
        if not file_path.endswith(".xlsx"):
            raise ValueError("file_name must end with .xlsx")
        try:
            file_client = self.file_system_client.get_file_client(file_path=file_path)
            fileBytesObject = file_client.download_file().readall()
            df = pd.read_excel(fileBytesObject, sheet_name=sheet_name)
            return df
        except Exception as e:
            print(e)

    def download_xml_file_from_directory(
        self, file_path: str, xpath: str = None, get_root: bool = False
    ) -> pd.DataFrame:
        file_client = self.file_system_client.get_file_client(file_path=file_path)
        fileBytesObject = file_client.download_file().readall()
        s = str(fileBytesObject, "utf-8")
        data = StringIO(s)

        if get_root:
            tree = ET.parse(data)
            root = tree.getroot()
            return root
        else:
            df = pd.read_xml(data, xpath=xpath)
            return df

    # TODO: Make sure overwriting the input files is not allowed
    def upload_df_as_csv(
        self, directory: str, file_name: str, data: pd.DataFrame
    ) -> None:
        """Upload pandas DataFrame as csv to an Azure blob container

        Args:
            directory (str): The directory to which we want to save the file
            filepath (str): the name of the flat file you want to convert your dataframe to (e.g., file_name.csv)
            data (pd.DataFrame): the dataframe you want to upload as csv
        """
        try:
            df_csv = data.to_csv(index=False)
            directory_client = self.file_system_client.get_directory_client(directory)
            file_client = directory_client.create_file(file_name)
            file_client.append_data(data=df_csv, offset=0, length=len(df_csv))
            file_client.flush_data(len(df_csv))

        except Exception as e:
            print(e)

    def upload_df_to_blob(self, df: pd.DataFrame, container: str, blob: str) -> None:
        """Upload pandas Dataframe as csv to an Azure Blob container allowing file sizes over 4mb

        Args:
            df (pd.DataFrame): the dataframe you want to upload as csv
            container (str): string of the container name
            blob (str): destination path of the csv
        """
        try:
            df_csv = StringIO
            df_csv = df.to_csv(index=False)
            blob_client = self.blob_service_client.get_blob_client(
                container=container, blob=blob
            )
            blob_client.upload_blob(df_csv, overwrite=True)

        except Exception as e:
            print(e)


def store_csv_locally(df: pd.DataFrame, file_name: str, directory: str):
    """Store csv files locally in a data-output folder that should not be pushed to the repo

    Args:
        df (pd.DataFrame): dataframe you want to store as csv
        file_name (str): name of the file you will store
        directory (str): storing location of the file
    """
    directory = f"data_output/{directory}/"
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)
    df.to_csv(f"{directory}/{file_name}.csv", index=False)


class SqlDatabase:
    """Database object to connect with SQL database"""

    # This connection option is defined by microsoft in msodbcsql.h
    SQL_COPT_SS_ACCESS_TOKEN = 1256
    DRIVER = "{ODBC Driver 17 for SQL Server}"
    PORT = 1433

    def __init__(self, server_name: str, database_name: str):
        """The constructor

        Args:
            server_name (str): name of server
            database_name (str): name of database
        """
        self.server_name = server_name
        self.database_name = database_name
        self.connection = None
        self._connection_string = None
        self._token_struct = None
        self._alchemy_engine = None
        # Initialize the connection
        self._create_connection()

    def _create_connection(self) -> None:
        """Create the pyodbc connection with the database.
        Additionally sets _connection_string and _token_struct for use in sqlalchemy connection
        """

        credential = DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
            exclude_visual_studio_code_credential=False,
            exclude_shared_token_cache_credential=True,
            exclude_interactive_browser_credential=True,
        )
        token_bytes = credential.get_token(
            "https://database.windows.net/.default"
        ).token.encode("UTF-16-LE")
        self._token_struct = struct.pack(
            f"<I{len(token_bytes)}s", len(token_bytes), token_bytes
        )
        self._connection_string = (
            f"Driver={SqlDatabase.DRIVER};"
            f"Server=tcp:{self.server_name},{SqlDatabase.PORT};"
            f"Database={self.database_name};"
            f"Encrypt=yes;TrustServerCertificate=no;"
            f"Connection Timeout=10;"
        )
        try:
            self.connection = pyodbc.connect(
                self._connection_string,
                attrs_before={SqlDatabase.SQL_COPT_SS_ACCESS_TOKEN: self._token_struct},
            )
        except Exception:
            logger.error("Error in connecting to database.")
            raise

    def run_database_query(
        self, sql_code: str, return_output: bool = False
    ) -> Optional[pd.DataFrame]:
        """Run a SQL query on the database.
        Can be used ot run query and create new table in database using a SELECT INTO query (return_output = False),
        or to return the result of the query as a pandas Dataframe (return_output = True).

        Args:
            sql_code (str): the SQL query to run
            return_output (bool, optional): Return the output of the query as a DataFrame. Defaults to False.

        Returns:
            Optional[pd.DataFrame]: The result of the query
        """

        # make connection and run SQL
        cursor = self.connection.cursor()

        try:
            cursor.execute(sql_code)

            # If there is data to return retrieve it and change into dataframe
            if return_output:
                data = cursor.fetchall()
                colnames = [desc[0].lower() for desc in cursor.description]
                return pd.DataFrame.from_records(data, columns=colnames)

            # Commit DB changes if needed (no output returned)
            self.connection.commit()
        except Exception:
            logger.error("Error in running database query.")
            raise
        finally:
            # Always close the cursor
            cursor.close()

    def _create_alchemy_engine(self) -> None:
        """Create sqlalchemy engine required for writing pandas dataframe to database"""
        self._alchemy_engine = sqlalchemy.create_engine(
            f"mssql+pyodbc:///?odbc_connect={self._connection_string}",
            fast_executemany=True,
            connect_args={
                "attrs_before": {
                    SqlDatabase.SQL_COPT_SS_ACCESS_TOKEN: self._token_struct
                }
            },
        )

    def write_dataframe_to_database(
        self,
        dataframe: pd.DataFrame,
        schema: str,
        table_name: str,
        if_exists: Literal["fail", "replace", "append"] = "fail",
        chunksize: int = 10000,
    ) -> None:
        """Write a pandas dataframe to the SQL database as a table.
            For performance an SQLalchemy engine and connection is used in combination for pandas to_sql function.

        Args:
            dataframe (pd.DataFrame): The pandas dataframe to write
            schema (str): Schema to which the table is written
            table_name (str): Name of the table to write
            if_exists (Literal["fail", "replace", "append"], optional): Define what happens if the table already exists. Defaults to "fail".
            chunksize (int, optional): Specify the number of rows in each batch to be written at a time. Defaults to 10000.
                The default setting is a good starting point, when Database errors (such as time-out errors) occur during writing, try to adjust the chunksize.

        Raises:
            ValueError: When optional `if_exists` is provided with an invalid input
        """
        # Validate input
        if if_exists not in ["fail", "replace", "append"]:
            raise ValueError(
                f"{if_exists} is not valid for if_exists, use: fail, replace, append"
            )

        # Create alchemy engine if it was not yet initiated
        if not self._alchemy_engine:
            self._create_alchemy_engine()

        # Write the data
        with self._alchemy_engine.connect() as alchemy_connection:
            dataframe.to_sql(
                table_name,
                alchemy_connection,
                schema=schema,
                index=False,
                if_exists=if_exists,
                chunksize=chunksize,
            )
