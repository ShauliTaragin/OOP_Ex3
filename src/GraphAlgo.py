from abc import ABC
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, file: str):
        self.graph = self.load_from_json(file)


    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph(file_name)

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass


