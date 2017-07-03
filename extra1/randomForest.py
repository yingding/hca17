# Random Forest Algorithm on Sonar Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt, log2
from crawler.downloadhelper import DownloadHelper

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, class_values):
    gini = 0.0
    for class_value in class_values:
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            proportion = [row[-1] for row in group].count(class_value) / float(size)
            gini += (proportion * (1.0 - proportion))
    # gini = sum(proportion) - sum(proportion^2) = 1 - sum(proportion^2), since sum(proportion) = 1
    return gini

# Calculate the entropy for a split dataset
def entropy(groups, class_values):
    entropy = 0.0
    for class_value in class_values:
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            proportion = [row[-1] for row in group].count(class_value) / float(size)
            if proportion == 0:
                continue
            entropy += (-proportion * log2(proportion))
    return entropy

# Select the best split point for a dataset
def get_split(dataset, n_features, cost_function):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    features = list()
    # get random sampling of n_features
    while len(features) < n_features:
        index = randrange(len(dataset[0])-1)
        if index not in features:
            features.append(index)
    # split test for each row to get the smallest cost, which means minimize the impurity
    # information gain is not used.
    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            cost = cost_function(groups, class_values)
            if cost < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], cost, groups
    # return the first node
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    # set the terminal leaf with the majority of counts among the class labels
    return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, n_features, depth, cost_function):
    # get the split group from node object, left subtree and right subtree
    # a binary split
    left, right = node['groups']
    del(node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        # get the best split and make a new node
        node['left'] = get_split(left, n_features, cost_function)
        # increase depth by 1 and call the sub tree split recursively
        split(node['left'], max_depth, min_size, n_features, depth+1, cost_function)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right, n_features, cost_function)
        split(node['right'], max_depth, min_size, n_features, depth+1, cost_function)

# Build a decision tree
def build_tree(train, max_depth, min_size, n_features, cost_function):
    # make the root node
    root = get_split(train, n_features, cost_function)
    # split root recursively
    split(root, max_depth, min_size, n_features, 1, cost_function)
    return root

# Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        # testing if it is a node, type of dict
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            # if it is a leaf, return the prediction class value
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

# Create a random subsample from the dataset with replacement
def subsample(dataset, ratio):
    sample = list()
    n_sample = round(len(dataset) * ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample

# Make a prediction with a list of bagged trees
def bagging_predict(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    # return the frequent class label from all tree prediction
    return max(set(predictions), key=predictions.count)

# Random Forest Algorithm
def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features, cost_function):
    trees = list()
    for i in range(n_trees):
        # bagging

        sample = subsample(train, sample_size)
        # print('Total training data size: {}, subsample size: {}'.format(len(train), len(sample)))
        # create a DT, with a given number_of_features, the random feature is sampled
        tree = build_tree(sample, max_depth, min_size, n_features, cost_function)
        trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
    return(predictions)

# Test the random forest algorithm
seed(1)

"""
load and prepare data
"""
# Data Set about the metal cylinder and cylindrical rocks
# Data Source https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+(Sonar,+Mines+vs.+Rocks)
dh = DownloadHelper(data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data", data_file_name="sonar.all-data")
data_path = dh.download_data()

# Print out the data_path
print(data_path)

dataset = load_csv(data_path)

# convert string attributes to float
for i in range(0, len(dataset[0])-1):
    str_column_to_float(dataset, i)

# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

"""
testing the algorithm
"""

# evaluate algorithm
n_folds = 5
max_depth = 10
# adjust the number of date in a leaf.
# set to 1, the class label of the last node shall be the prediction value.
min_size = 1
# sample_ratio = 1.0 # use the whole sample
sample_ratio = 1.0
n_features = int(sqrt(len(dataset[0])-1))

# with gini_index
print("#### Gini index as split function, no bagging")
for n_trees in [1, 5, 10]:
    scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth, min_size, sample_ratio, n_trees, n_features, gini_index)
    print('Trees: %d' % n_trees)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# with entropy
print("\n#### Entropy as split function, no bagging")
for n_trees in [1, 5, 10]:
    scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth, min_size, sample_ratio, n_trees, n_features, entropy)
    print('Trees: %d' % n_trees)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# with entropy and bagging
sample_ratio = 0.7
print("\n#### Entropy as split function, with bagging")
for n_trees in [1, 5, 10]:
    scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth, min_size, sample_ratio, n_trees, n_features, entropy)
    print('Trees: %d' % n_trees)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# Todo: Adopt this data set to sci-kit learn tree classifier for classification and random forest


