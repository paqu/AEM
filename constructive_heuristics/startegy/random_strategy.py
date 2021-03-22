import random

import numpy as np

from constructive_heuristics.cycle import Cycle
from constructive_heuristics.startegy.strategy import Strategy


class RandomStrategy(Strategy):
    def do_algorithm(self, distance_matrix):
        vert_list = np.random.randint(0, 100, 10)
        vert_list = np.append(vert_list, vert_list[0])

        return Cycle(vert_list, random.randint(0, 1000))