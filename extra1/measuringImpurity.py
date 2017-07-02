from math import log2
from matplotlib import pyplot as plt

def maximum_entropy (num_classes):
    """
    :param num_classes:
    :return:
    """
    # entropy reach its maximum value, while all classes have equal probability
    p = equal_class_probability(num_classes)
    return -num_classes * p * log2(p)

def equal_class_probability(num_classes):
    return float(1/num_classes)

def maximum_gini_index (num_classes):
    """

    :param num_classes:
    :return:
    """
    # gini index reach its maximum value, while all classes have equal probability
    p = equal_class_probability(num_classes)
    return 1 - num_classes * p * p



num_classes_array = list(range(1,17))

# fig, ax1 = plt.subplots()
# red_line, = ax1.plot(num_classes_array, [maximum_entropy(n) for n in num_classes_array], 'ro-', label='max_entropy')
# ax1.set_xlabel('Number of classes')
# ax1.set_ylabel('Maximum Entropy', color='r')
# ax1.tick_params('y', color='r')
#
# # ax1.set_ylim([0,6])
#
# ax2 = ax1.twinx()
# blue_line, = ax2.plot(num_classes_array, [equal_class_probability(n) for n in num_classes_array], 'bo-', label='probability')
# ax2.set_ylabel('probability (equal for all classes)', color='b')
# ax2.tick_params('y', color='b')
#
# fig.tight_layout()
# # handles, labels = ax1.get_legend_handles_labels()
# # ax1.legend(handles, labels)
# # handles, labels = ax2.get_legend_handles_labels()
# # ax2.legend(handles, labels)
# plt.legend(handles=[red_line, blue_line],loc=10) # legend location from https://matplotlib.org/1.3.0/users/legend_guide.html
# plt.grid(True)
# plt.title('Max Entropy & Probablilty relating to Number of Classes')
# plt.show()

def display_plots(num_classes_array, y_function1, y_function2, y_label1, y_label2, legend1, legend2, title):
    # num_classes_array = list(range(1,17))

    fig, ax1 = plt.subplots()
    red_line, = ax1.plot(num_classes_array, [y_function1(n) for n in num_classes_array], 'ro-', label=legend1)
    ax1.set_xlabel('Number of classes')
    ax1.set_ylabel(y_label1, color='r')
    ax1.tick_params('y', color='r')

    # ax1.set_ylim([0,6])

    ax2 = ax1.twinx()
    blue_line, = ax2.plot(num_classes_array, [y_function2(n) for n in num_classes_array], 'bo-', label=legend2)
    ax2.set_ylabel(y_label2, color='b')
    ax2.tick_params('y', color='b')

    fig.tight_layout()
    # handles, labels = ax1.get_legend_handles_labels()
    # ax1.legend(handles, labels)
    # handles, labels = ax2.get_legend_handles_labels()
    # ax2.legend(handles, labels)
    plt.legend(handles=[red_line, blue_line],loc=10) # legend location from https://matplotlib.org/1.3.0/users/legend_guide.html
    plt.grid(True)
    plt.title(title)
    plt.show()

# Example similar to http://people.revoledu.com/kardi/tutorial/DecisionTree/how-to-measure-impurity.htm
# plot of max entropy and probability relating to number of classes
display_plots(num_classes_array, maximum_entropy, equal_class_probability, y_label1='Maximum Entropy', y_label2='probability (equal for all classes)', legend1='max_entropy', legend2='probability', title='')
# plot of max gini index and probability relating to number of classes
display_plots(num_classes_array, maximum_gini_index, equal_class_probability, y_label1='Maximum Gini Index', y_label2='probability (equal for all classes)', legend1='max_gini', legend2='probability', title='')
