import wget
import os
from typing import Any



class DownloadHelper:
    bosten_housing_data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
    directory = "data"
    bosten_housing_file_name = "housing.data"
    @classmethod
    def download_data(cls, url: str, debug=False):
        data_dir = cls.download_directory_path()
        data_path = cls.bosten_housing_file_path()
        if not os.path.exists(data_dir):
            # create the download directory if it exists
            os.makedirs(data_dir)
        if not os.path.isfile(data_path):
            wget.download(cls.bosten_housing_data_url, out=data_dir)
            return data_path
        return ""

    @classmethod
    def bosten_housing_file_path(cls):
        return os.path.abspath(
            os.path.join(cls.download_directory_path(), cls.bosten_housing_file_name)
        )

    @classmethod
    def download_directory_path(cls):
        """
        get the absolute path of week5/data directory
        :return:
        """
        return os.path.abspath(
            # use dirname to get to the parent directory of crawler
            os.path.join(os.path.dirname(cls.parent_dir()), cls.directory)
        )

    @classmethod
    def parent_dir(cls):
        """
        :return: the absolute path of the directory of this file, the absolute path of crawler module
        """
        # file is absolute, os.curdir() and os.pardir() is relative
        return os.path.dirname(__file__)