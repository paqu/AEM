class Cycle:
    def __init__(self, vertex_list, length):
        self._vertex_list = vertex_list
        self._length = length

    @property
    def cycle(self):
        return self._vertex_list

    @property
    def length(self):
        return self._length

    def __str__(self):
        return f"({self._length}, {self._vertex_list})\n"

    def __repr__(self):
        return f"({self._length}, {self._vertex_list})\n"

    @staticmethod
    def calculate_cycle_length(distance_matrix, vertex_list):
        vertex_list_length = len(vertex_list)
        if vertex_list_length < 2:
            return 0

        cycle_length = 0
        for it in range(vertex_list_length - 1):
            first_vertex = vertex_list[it]
            second_vertex = vertex_list[it + 1]
            cycle_length += distance_matrix[first_vertex, second_vertex]

        cycle_length += distance_matrix[vertex_list[-1], vertex_list[0]]
        return cycle_length
