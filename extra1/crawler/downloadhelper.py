import wget
import os

class DownloadHelper(object):
    def __init__(self, data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data", data_file_name="sonar.all-data",directory="data"):
        self.data_url = data_url
        self.directory = directory
        self.data_file_name = data_file_name

    def download_data(self, debug=False):
        data_dir = self.download_directory_path()
        data_path = self.data_file_path()
        if not os.path.exists(data_dir):
            # create the download directory if it exists
            os.makedirs(data_dir)
        if not os.path.isfile(data_path):
            wget.download(self.data_url, out=data_dir)
        # always return the data_path
        return data_path

    def data_file_path(self):
        return os.path.abspath(
            os.path.join(self.download_directory_path(), self.data_file_name)
        )

    def download_directory_path(self):
        """
        get the absolute path of week5/data directory
        :return:
        """
        return os.path.abspath(
            # use dirname to get to the parent directory of crawler
            os.path.join(os.path.dirname(self.parent_dir()), self.directory)
        )

    def parent_dir(self):
        """
        :return: the absolute path of the directory of this file, the absolute path of crawler module
        """
        # file is absolute, os.curdir() and os.pardir() is relative
        return os.path.dirname(__file__)