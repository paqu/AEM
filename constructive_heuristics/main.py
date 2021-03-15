import numpy as np

from constructive_heuristics.cycle import Cycle
from constructive_heuristics.startegy.greedy_cycle_strategy import GreedyCycleStrategy
from constructive_heuristics.startegy.greedy_nearest_neighbor import GreedyNearestNeighbor


def main():
    distance_matrix = np.array([
        [0, 1, 2, 3, 4],
        [1, 0, 2, 3, 4],
        [2, 2, 0, 3, 4],
        [3, 3, 3, 0, 4],
        [4, 4, 4, 4, 0]])
    vertex_list = np.array([0, 1, 2])
    length = Cycle.calculate_cycle_length(distance_matrix, vertex_list)
    strategy = GreedyNearestNeighbor()
    result = strategy.do_algorithm(distance_matrix)
    print(length)
    print(result)


if __name__ == '__main__':
    main()
