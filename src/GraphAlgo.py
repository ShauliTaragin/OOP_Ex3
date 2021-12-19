import _json
import json
from abc import ABC
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, graph:DiGraph = None):
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
            str_pos = str_pos.replace(" ","")
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
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass
