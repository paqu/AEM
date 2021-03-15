import numpy as np

from constructive_heuristics.cycle import Cycle
from constructive_heuristics.startegy.strategy import Strategy


class RegretStrategy(Strategy):
    VERTEX_RATIO = 0.5
    K = 2

    def do_algorithm(self, distance_matrix):
        pass
