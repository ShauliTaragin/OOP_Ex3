import GeoLocation


class Node:

    def __init__(self, key: int, geolocation: GeoLocation):
        self.key = key
        self.weight = 0
        self.geolocation = geolocation
        self.tag = 0
        self.outEdges = {}
        self.inEdges = {}

    def __str__(self):
        return self.key

    def addOutEdge(self, weight: float, Dest: int):

        self.outEdges[Dest] = weight

    def addinEdge(self, weight: float, Src: int):

        self.inEdges[Src] = weight
