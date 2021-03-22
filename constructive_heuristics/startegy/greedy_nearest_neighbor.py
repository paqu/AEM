import numpy as np

from constructive_heuristics.cycle import Cycle
from constructive_heuristics.startegy.strategy import Strategy


class GreedyNearestNeighbor(Strategy):
    VERTEX_RATIO = 0.5

    def do_algorithm(self, distance_matrix):
        vertex_list = np.array([np.random.randint(len(distance_matrix))])
        shortest_cycle = Cycle(vertex_list, Cycle.calculate_cycle_length(distance_matrix,
                                                                         vertex_list))
        while len(vertex_list) / len(distance_matrix) < GreedyNearestNeighbor.VERTEX_RATIO:
            shortest_cycle = GreedyNearestNeighbor.__find_nearest_neighbor(distance_matrix, vertex_list)
            vertex_list = shortest_cycle.cycle
        return shortest_cycle

    @staticmethod
    def __find_nearest_neighbor(distance_matrix, vertex_list):
        remaining_vertex_list = np.delete(np.arange(len(distance_matrix)), vertex_list)
        last_vertex = vertex_list[-1]
        distance_list = np.copy(distance_matrix[last_vertex])
        remaining_distance_list = np.copy(distance_list[remaining_vertex_list])
        min_length = np.min(remaining_distance_list)
        nearest_neighbor = np.where(distance_list == min_length)[0][0]
        new_vertex_list = np.append(vertex_list, nearest_neighbor)

        return Cycle(new_vertex_list, Cycle.calculate_cycle_length(distance_matrix,
                                                                   new_vertex_list))
