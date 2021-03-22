import numpy as np
from ..cycle import Cycle
from ..strategy import Strategy


class NNStrategy(Strategy):
    def do_algorithm(self, matrix, startPoint=0, stop=50):
        dist_matrix = matrix.copy()

        size, _ = dist_matrix.shape
        tour = []
        distance = 0

        i = startPoint
        tour.append(i)
        dist_matrix[:, i] = 2**32 - 1

        while len(tour) != stop and len(tour) < size:
            j = np.argmin(dist_matrix[i, :])
            tour.append(j)
            distance += matrix[i, j]
            dist_matrix[:, j] = 2**32 - 1
            dist_matrix[j, i] = 2**32 - 1
            i = j

        distance += matrix[tour[0], tour[-1]]
        tour.append(tour[0])

        return Cycle(tour, distance)
