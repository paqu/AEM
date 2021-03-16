import numpy as np
import math
import matplotlib.pyplot as plt

def distance_matrix(values, calculate):
    size = len(values)
    matrix = np.zeros((size,size), dtype=np.uint32)

    for i, start in enumerate(values):
        for j, end in enumerate(values):
            matrix[i,j] = calculate(start, end, round=math.ceil)

    return matrix


def plot_result(graph_cord, solution, filename=None, title="Title"):

    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize = (7,7))
    plt.title(title, fontdict=font)
    X = []
    Y = []
    labels = []

    for x, y, label in solution:
        X.append(x)
        Y.append(y)
        labels.append(label)


    ALL_Y = [node[1] for node in graph_cord]
    ALL_X = [node[0] for node in graph_cord]

    #all cities
    plt.scatter(ALL_X, ALL_Y)

    #solution path
    plt.plot(X, Y,"or-")

    #print labels
    for i in range(len(solution)):
        plt.text(X[i], Y[i], labels[i], fontsize=15)

    if filename:
        plt.savefig(filename)

    #plt.show()
