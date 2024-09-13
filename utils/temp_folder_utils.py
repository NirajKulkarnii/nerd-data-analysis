import shutil
import os


def create_temp_folder(folder_path='../screenshot_data/temp'):
    """
    Creates a temporary folder if it does not already exist.

    Args:
        folder_path (str): The path to the folder to create. Default is './temp'.
    """
    # Check if the folder already exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def delete_temp_folder(folder_path='../screenshot_data/temp'):
    """
    Deletes the specified folder and its contents if it exists.

    Args:
        folder_path (str): The path to the folder to delete. Default is './temp'.
    """
    # Check if the folder exists, and delete it along with its contents
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
