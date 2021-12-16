class Node:

    def __init__(self, _key: int, _geolocation: tuple):
        self._key = _key
        self._weight = 0;
        self._geolocation = _geolocation
        self._tag = 0
        self._outEdges = {}
        self._inEdges = {}

    def __str__(self):
        return self._key

    def addOutEdge(self, weight : float, Dest:int):
        self._outEdges[Dest] = weight

    def addinEdge(self,weight:float , Src:int):
        self._inEdges[Src] = weight



