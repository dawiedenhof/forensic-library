"""Utility functions that can be used within the project"""

import hashlib
import logging
import os

import pandas as pd
from cryptography.fernet import Fernet


def get_logger(name: str) -> logging.Logger:
    """Returns a logger instance with a name you can specify

    Args:
        name (str): Name of your logger

    Returns:
        logging.Logger: Logger object based on python logging module
    """
    logger = logging.getLogger(name)

    if not logger.handlers:  # Logger not yet configured
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(
            logging.Formatter(
                fmt="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
                datefmt="%d-%b-%y %H:%M:%S",
            )
        )
        logger.addHandler(ch)

    return logger


def hash_sha256(self, input_string: str) -> str:
    """Create a 256 byte hash string for an existing string

    Args:
        input_string (str): string to be hashed

    Returns:
        str: hashed string
    """
    hash_object = hashlib.sha256()
    hash_object.update(input_string.encode())
    return hash_object.hexdigest()


def encrypt_string(input_string: str) -> str:
    """Encrypt string based on a pre-generated Fernet key

    Args:
        input_string (str): String to be encrypted

    Returns:
        str: Encrypted string
    """
    with open("./keys/myfernet.key", "rb") as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    encrypted_string = cipher.encrypt(input_string.encode())
    return encrypted_string.decode("utf-8")


def decrypt_string(encrypted_input_string: str) -> str:
    """Decrypt string based on an encrypted string

    Args:
        encrypted_input_string (str): Encrypted string to be decrypted
    Returns:
        str: Decrypted string
    """
    with open("./keys/myfernet.key", "rb") as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    decrypted_string = cipher.decrypt(encrypted_input_string)
    return decrypted_string.decode("utf-8")


def write_data(path: str, file_name: str, data: pd.DataFrame):
    """Check if folder to write to exist, create folder if it doesn't and write to said folder

    Args:
        path (str): Path of the folder
        file_name (str): File name of the written data
        data (pd.DataFrame): DataFrame to write to folder
    """

    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, file_name)

    data.to_csv(file_path, index=False)
