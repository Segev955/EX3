import matplotlib.pyplot as plt
import numpy as np


class Diagram:
    # ***************************************Center*********************************

    labels = ['G1', 'G2', 'G3', '1000', '10000']
    java = [0.002, 0.003, 3.800, 0, 0]
    python = [0.001, 0.004, 0.021, 0, 0]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, java, width, label='Java')
    ax.bar(x, python, width, label='Python')

    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_ylabel('leftTitle')
    ax.set_title('Center')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()

    # ********************************Short Path**********************************

    labels = ['G1', 'G2', 'G3', '1000', '10000']
    java = [0.002, 0.002, 0.003, 0.068, 1.133]
    python = [0.001, 0.001, 0.001, 0.122, 1.35]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, java, width, label='Java')
    ax.bar(x, python, width, label='Python')

    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_ylabel('leftTitle')
    ax.set_title('Short Path')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()

    # ***********************************Load*************************************

    labels = ['G1', 'G2', 'G3', '1000', '10000']
    java = [0.050, 0.057, 0.063, 0.162, 0.481]
    python = [0.001, 0.001, 0.001, 0.026, 0.203]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, java, width, label='Java')
    ax.bar(x, python, width, label='Python')

    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_ylabel('leftTitle')
    ax.set_title('Load')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()

    # ***************************************Save**********************************

    labels = ['G1', 'G2', 'G3', '1000', '10000']
    java = [0.030, 0.034, 0.037, 0.110, 0.336]
    python = [0.001, 0.001, 0.002, 0.110, 1.102]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, java, width, label='Java')
    ax.bar(x, python, width, label='Python')

    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_ylabel('leftTitle')
    ax.set_title('Save')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()

    # ***************************************TSP*********************************

    labels = ['G1', 'G2', 'G3', '1000', '10000']
    java = [0.001, 0.001, 0.010, 0.219, 4.833]
    python = [0.001, 0.005, 0.009, 2.692, 0]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, java, width, label='Java')
    ax.bar(x, python, width, label='Python')

    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_ylabel('leftTitle')
    ax.set_title('TSP')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()

if __name__ == '__main__':
    Diagram()
