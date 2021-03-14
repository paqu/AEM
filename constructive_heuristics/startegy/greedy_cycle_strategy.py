import numpy as np

from constructive_heuristics.cycle import Cycle
from constructive_heuristics.startegy.strategy import Strategy


class GreedyCycleStrategy(Strategy):
    VERTEX_RATIO = 0.5

    def do_algorithm(self, distance_matrix):
        vertex_list = np.array([np.random.randint(len(distance_matrix))])
        shortest_cycle = Cycle(vertex_list, Cycle.calculate_cycle_length(distance_matrix,
                                                                         vertex_list))
        while len(vertex_list) / len(distance_matrix) < GreedyCycleStrategy.VERTEX_RATIO:
            shortest_cycle = GreedyCycleStrategy.__find_shortest_cycle(distance_matrix, vertex_list)
            vertex_list = shortest_cycle.cycle
        return shortest_cycle

    @staticmethod
    def __find_shortest_cycle(distance_matrix, vertex_list):
        remaining_vertex_list = np.delete(np.arange(len(distance_matrix)), vertex_list)

        cycle_list = np.array([])
        for vertex in remaining_vertex_list:
            new_vertex_list = np.append(vertex_list, vertex)
            cycle_list = np.append(cycle_list,
                                   Cycle(new_vertex_list,
                                         Cycle.calculate_cycle_length(distance_matrix,
                                                                      new_vertex_list)))

        return min(cycle_list, key=lambda cycle: cycle.length)
