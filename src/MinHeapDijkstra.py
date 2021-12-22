import copy
import sys

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.Node import Node
from src.minHeap import MinHeap


class DijkstraUsingMinHeap:
    class Graph:
        def __init__(self, Graph_algo: GraphAlgo):
            self.graph: DiGraph = copy.deepcopy(Graph_algo.graph)
            self.max = 0
            self.parents = []
            self.heap_nodes = []
            self.extracted = []

        def dijkstra_GetMinDistances(self, source_vertex: int, dest: int = None):
            self.max = 0
            INFINITY = sys.maxsize
            index1 = 0
            # find the node with the max id
            for index in self.graph.nodes.keys():
                if index > index1:
                    index1 = index
            # init the list with the max node id
            self.parents = [0] * (index1 + 1)
            self.extracted = [False] * (index1 + 1)
            self.heap_nodes = [INFINITY] * (index1 + 1)
            self.parents[source_vertex] = source_vertex
            minHeap = MinHeap(self.graph.v_size(), source_vertex, self.graph, (index1 + 1))
            # iterate over the nodes and add them to the heap
            for key in self.graph.nodes.keys():
                if key != source_vertex:
                    minHeap.insert(self.graph.nodes.get(key))
            self.heap_nodes[source_vertex] = 0
            # while minHeap is not empty
            while not minHeap.isEmpty():
                # extract the min
                extractedNode: Node = minHeap.extractMin()
                # get the extracted vertex
                extractedNodeKey = extractedNode.key
                self.extracted[extractedNodeKey] = True
                if extractedNodeKey == dest:
                    return
                # iterate through all the adjacent vertices
                dict_temp = self.graph.all_out_edges_of_node(extractedNodeKey)
                for edges in dict_temp.keys():
                    destination = edges
                    weight_of_node = dict_temp.get(destination)
                    # only if destination vertex is not present in SPT
                    if self.extracted[destination] == False:
                        newDest = self.heap_nodes[extractedNodeKey] + weight_of_node
                        currentDest = self.heap_nodes[destination]
                        # if the currentDest is bigger then the newDest, update the min dist and update the parent
                        if currentDest > newDest:
                            self.decreaseKey(minHeap, newDest, destination)
                            self.heap_nodes[destination] = newDest
                            # switch the previous parent of the destination
                            self.parents[destination] = extractedNodeKey
                # the last Node to be extracted is the one with the biggest weight
            self.max = minHeap.node_holder1[0].weight

        def decreaseKey(self, minHeap: MinHeap, newKey, vertex: int):
            # get the index which distance's needs a decrease;
            index = minHeap.index_of_nodes1[vertex]
            # get the node and update its value
            node: Node = minHeap.node_holder1[index]
            node.weight = newKey
            minHeap.heapfyUp(index)
