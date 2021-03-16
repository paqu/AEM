import tsplib95

from .utils import distance_matrix, plot_result

class Instance():
    def __init__(self, strategy, description=""):
        self._strategy = strategy
        self._coordinates = []
        self._labels = []
        self._solutions = []
        self._description = description
        self._distance_matrix = None


    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    @property
    def solutions(self):
        return self._solutions

    @property
    def distance_matrix(self):
        return self._distance_matrix

    @property
    def labels(self):
        return self._labels

    @property
    def coordinates(self):
        return self._coordinates

    def load_problem(self, filename):
        problem = tsplib95.load(filename)
        coord   = problem.as_name_dict().get('node_coords')
        self._labels       = list(coord.keys())
        self._coordinates  = list(coord.values())
        self._distance_matrix = distance_matrix(self._coordinates, tsplib95.distances.euclidean)


    def run(self, num=50):
        for i in range(num):
            result = self._strategy.do_algorithm()
            self._solutions.append(result)

        self._solutions = sorted(self._solutions, key=lambda solution: solution.length)


    def get_min(self):
        return self._solutions[0].length

    def get_max(self):
        return self._solutions[-1].length

    def get_avg(self):
        return sum(solution.length for solution in self._solutions)/len(self._solutions)


    def save_to_file(self, filename=None):
        solution_to_print = []
        for i in self._solutions[0].cycle:
            solution_to_print.append((*self._coordinates[i], str(self._labels[i])))

        title = self._description + ", "if self._description else ""
        title += "distance: " + str(self._solutions[0].length)

        plot_result(self._coordinates, solution_to_print, filename=filename, title=title)
