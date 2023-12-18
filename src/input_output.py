"""Data loading and writing module for the Baobab analysis
"""

import os

# Import libraries necessary for the analysis
from io import StringIO

import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient


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
        self, file_path: str
    ) -> pd.DataFrame:  # the name of the file path (e.g., folder/file_name.csv)
        """Download csv files from a specific location within the blob container

        Args:
            file_path (str): the path to the flat file you want to download (e.g., folder/file_name.csv)

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
            df = pd.read_csv(data, sep=";")
            return df
        except Exception as e:
            print(e)

    # Function to download a csv file from Azure
    def download_xlsx_file_from_directory(
        self, file_path: str
    ) -> pd.DataFrame:  # the name of the file path (e.g., folder/file_name.xlsx)
        if not file_path.endswith(".xlsx"):
            raise ValueError("file_name must end with .xlsx")
        try:
            file_client = self.file_system_client.get_file_client(file_path=file_path)
            fileBytesObject = file_client.download_file().readall()
            df = pd.read_excel(fileBytesObject)
            return df
        except Exception as e:
            print(e)

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
