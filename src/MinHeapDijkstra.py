import copy
import sys

from DiGraph import DiGraph
from Node import Node
from minHeap import MinHeap
from src.GraphAlgo import GraphAlgo
class DijkstraUsingMinHeap:
    class Graph:
        def __init__(self, Graph_algo: GraphAlgo):
            self.graph: DiGraph = copy.deepcopy(Graph_algo.graph)
            self.max = 0
            self.parents = {}
            self.heap_nodes = {}
            self.extracted = {}

        def dijkstra_GetMinDistances(self, source_vertex: int, dest:int =None):
            self.max = 0
            INFINITY = sys.maxsize
            self.parents.clear()
            self.heap_nodes.clear()
            self.extracted.clear()
            # for node in self.graph.nodes.keys():
            #
            self.parents[source_vertex] = source_vertex
            minHeap = MinHeap(self.graph.v_size(), source_vertex, self.graph)
            # // iterate over the nodes and add them to the heap
            for key in self.graph.nodes.keys():
                if (key != source_vertex):
                    minHeap.insert(self.graph.nodes.get(key))
                    self.heap_nodes[key] = INFINITY
                    self.extracted[key]=False
            self.heap_nodes[source_vertex] = 0
            # //while minHeap is not empty
            while (minHeap.isEmpty() == False):
                # //extract the min
                extractedNode: Node = minHeap.extractMin()
                # //extracted vertex
                extractedNodeKey = extractedNode.key
                self.extracted[extractedNodeKey] = True
                if (extractedNodeKey == dest):
                    return
                # //iterate through all the adjacent vertices
                for edges in self.graph.all_out_edges_of_node(extractedNodeKey).keys():
                    destination = edges
                    weight_of_node = self.graph.all_out_edges_of_node(extractedNodeKey).get(destination)
                    # //only if destination vertex is not present in SPT
                    if (self.extracted.get(destination)== False):
                        newDest = self.heap_nodes.get(extractedNodeKey) + weight_of_node
                        currentDest = self.heap_nodes.get(destination)
                        # //if the currentDest is bigger then the newDest, update the min dist and update the parent
                        if (currentDest > newDest):
                            self.decreaseKey(minHeap, newDest, destination)
                            self.heap_nodes[destination] = newDest
                            # //switch the previous parent of the destination
                            self.parents[destination] = extractedNodeKey

                # // the last Node to be extracted is the one with the biggest weight
            # for i in self.heap_nodes.keys():
            #    if( self.max<self.heap_nodes.get(i)):
            #        self.max=self.heap_nodes.get(i)
            self.max = minHeap.node_holder[0].weight

        def decreaseKey(self, minHeap: MinHeap, newKey, vertex: int):
            # //get the index which distance's needs a decrease;
            index = minHeap.index_of_nodes.get(vertex)
            # //get the node and update its value
            node: Node = minHeap.node_holder.get(index)
            node.weight = newKey
            minHeap.heapfyUp(index)
