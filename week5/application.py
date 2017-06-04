import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from crawler.downloadhelper import DownloadHelper
import os

# The dataset is in fact not in CSV format in the UCI Machine Learning Repository, the attributes are instead separated by whitespace. We can load this easily using the pandas library. We can then split the input (X) and output (Y) attributes so that they are easier to model with Keras and scikit-learn.

data_dir = DownloadHelper.download_directory_path()
print(data_dir)

# get the default data_url for the bosten_housing
data_url = DownloadHelper.bosten_housing_data_url

# download the data file
data_path = DownloadHelper.download_data(data_url)
print(data_path)

# load dataset
dataframe = pandas.read_csv(data_path, delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]

# define base model
def baseline_model():
    # create sequential model
    model = Sequential()
    # hidden layer
    model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
    # output layer
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# It is a simple model that has a single fully connected hidden layer with the same number of neurons as input attributes (13). The network uses good practices such as the rectifier activation function for the hidden layer. No activation function is used for the output layer because it is a regression problem and we are interested in predicting numerical values directly without transform.


# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=5, verbose=0)

kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

# Reasonable performance for models evaluated using Mean Squared Error (MSE) are around 20 in squared thousands of dollars (or $4,500 if you take the square root). This is a nice target to aim for with our neural network model.


