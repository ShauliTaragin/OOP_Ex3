class Node:

    def __init__(self, key: int, geolocation: tuple = (0, 0, 0)):
        self.key = key
        self.weight = 0
        self.geolocation = geolocation
        self.tag = 0
        self.outEdges = {}
        self.inEdges = {}

    def __repr__(self):
        return "{}".format(self.key)

    def __str__(self):
        return "{}".format(self.key)

    def add_out_edge(self, weight: float, dest: int):
        self.outEdges[dest] = weight

    def adding_edge(self, weight: float, src: int):
        self.inEdges[src] = weight
