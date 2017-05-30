from crawler.downloadhelper import DownloadHelper

data_url = DownloadHelper.bosten_housing_data_url
data_path = DownloadHelper.download_data(data_url)

# more infos about the data set can be found
# https://archive.ics.uci.edu/ml/datasets/Housing


