import numpy as np

from constructive_heuristics.cycle import Cycle
from constructive_heuristics.startegy.strategy import Strategy


class RegretStrategy(Strategy):
    VERTEX_RATIO = 0.5
    K = 2

    def do_algorithm(self, distance_matrix):
        vertex_list = np.array([np.random.randint(len(distance_matrix))])
        shortest_cycle = Cycle(vertex_list, Cycle.calculate_cycle_length(distance_matrix,
                                                                         vertex_list))
        while len(vertex_list) / len(distance_matrix) < RegretStrategy.VERTEX_RATIO:
            shortest_cycle = RegretStrategy.__find_max_regret_cycle(distance_matrix, vertex_list)
            vertex_list = shortest_cycle.cycle
        return shortest_cycle

    @staticmethod
    def __find_max_regret_cycle(distance_matrix, vertex_list):
        regrets_list = np.array([])
        remaining_vertex_list = np.delete(np.arange(len(distance_matrix)), vertex_list)
        for vertex in remaining_vertex_list:
            regret = RegretStrategy.__calculate_regret(distance_matrix, vertex, remaining_vertex_list)
            regrets_list = np.append(regrets_list, {'vertex': vertex, 'regret': regret})

        max_regret = max(regrets_list, key=lambda regret_dict: regret_dict['regret'])
        new_vertex_list = np.append(vertex_list, max_regret['vertex'])
        return Cycle(new_vertex_list, Cycle.calculate_cycle_length(distance_matrix,
                                                                   new_vertex_list))

    @staticmethod
    def __calculate_regret(distance_matrix, first_vertex, remaining_vertex_list):
        distance_list = np.copy(distance_matrix[first_vertex])
        remaining_distance_list = np.copy(distance_list[remaining_vertex_list])
        sorted_distance_list = np.sort(remaining_distance_list)
        i = 0
        regret = 0
        for distance in sorted_distance_list:
            if i >= RegretStrategy.K:
                return regret
            regret -= distance
            i += 1
        return regret
