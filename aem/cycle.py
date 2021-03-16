class Cycle():
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
