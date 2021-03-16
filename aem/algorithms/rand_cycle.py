import numpy as np
import random
from ..cycle import Cycle
from ..strategy import Strategy

class RandomStrategy(Strategy):
    def do_algorithm(self):
        vert_list = np.random.randint(0,100, 10)
        vert_list = np.append(vert_list, vert_list[0])

        return Cycle(vert_list, random.randint(0,1000))
