import _json
import json
import sys
from abc import ABC
from typing import List

import MinHeapDijkstra
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph(file_name)
        if self.graph is not None:
            return True
        else:
            return False

    def save_to_json(self, file_name: str) -> bool:
        NodesArray = []
        EdgesArray = []
        dictionary = {}
        for i in self.graph.nodes.keys():
            node_temp = self.graph.nodes.get(i)
            node_temp: Node
            nodes_dict = {}
            str_pos = node_temp.geolocation.__str__()
            str_pos = str_pos.replace(" ", "")
            str_pos = str_pos.replace("(", "")
            str_pos = str_pos.replace(")", "")
            nodes_dict["pos"] = str_pos
            nodes_dict["id"] = i
            NodesArray.append(nodes_dict)
            for j in node_temp.outEdges.keys():
                edge_dict = {}
                w = node_temp.outEdges.get(j)
                edge_dict["src"] = i
                edge_dict["w"] = w
                edge_dict["dst"] = j
                EdgesArray.append(edge_dict)
        dictionary["Edges"] = EdgesArray
        dictionary["Nodes"] = NodesArray
        try:
            with open(file_name, 'w') as f:
                json.dump(dictionary, f)
                f.close()
            return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list_of_path = []
        g_algo = GraphAlgo(self.graph)
        dijkstra_result = MinHeapDijkstra.DijkstraUsingMinHeap.Graph(g_algo)
        try:
            dijkstra_result.dijkstra_GetMinDistances(id1)
            if(dijkstra_result.heap_nodes[id2] == sys.maxsize):
                raise Exception()
            index = id2
            while(index != id1):
                list_of_path.insert(0, index)
                index = dijkstra_result.parents[index]
            list_of_path.insert(0, id1)
            ans = (dijkstra_result.heap_nodes[id2],list_of_path)
            return ans
        except:
            return ("inf", [])

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        min_max_value = sys.maxsize
        index = 0
        g_algo = GraphAlgo(self.graph)
        g1 = MinHeapDijkstra.DijkstraUsingMinHeap.Graph(g_algo)
        for i in self.graph.nodes.keys():
            g1.dijkstra_GetMinDistances(i)
            if (g1.max < min_max_value):
                min_max_value = g1.max
                index = i
        ans = (index, min_max_value)
        return ans

    def plot_graph(self) -> None:
        pass
