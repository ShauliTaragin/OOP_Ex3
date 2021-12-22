import copy
import json
import math
import sys

import pygame
from abc import ABC
from math import inf
from queue import Queue
from typing import List

# import HelperAlgo
import MinHeapDijkstra
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
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
                edge_dict["dest"] = j
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
            if dijkstra_result.heap_nodes[id2] == sys.maxsize:
                raise Exception()
            index = id2
            while index != id1:
                list_of_path.insert(0, index)
                index = dijkstra_result.parents[index]
            list_of_path.insert(0, id1)
            ans = (dijkstra_result.heap_nodes[id2], list_of_path)
            return ans
        except:
            return inf, []

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        actual_nodes_lst = []
        for i in node_lst:
            actual_nodes_lst.append(self.graph.nodes.get(i))
        if not self.findpath(actual_nodes_lst, self.graph):
            return None
        try:
            bestPath = []
            minPath = sys.maxsize
            for j in range(len(actual_nodes_lst)):
                holdCities = actual_nodes_lst.copy()
                current = 0
                path = []
                srcI = j
                destI, currentdest = 0, 0
                src = actual_nodes_lst[srcI].key
                holdCities.pop(srcI)
                path.append(self.graph.nodes[src].key)
                ans: float
                while holdCities:
                    minDist = sys.maxsize
                    for i in range(len(holdCities)):
                        a: Node
                        a = self.graph.nodes[src]
                        ans = 0
                        if (holdCities[i].key not in path):
                            b = self.shortest_path(src, holdCities[i].key)
                            ans = b[0]  # might be mistake here
                        dist = ans
                        if (dist != inf):
                            if dist < minDist:
                                minDist = dist
                                currentdest = holdCities[i].key
                                destI = i
                        else:
                            break
                    current += minDist
                    tempPath = self.shortest_path(src, currentdest)[1]  # mistake here , notice shortest path return
                    # list of int
                    if tempPath is None:
                        return None
                    flag_first = True
                    for n in tempPath:
                        if flag_first:
                            flag_first = False
                        else:
                            path.append(n)
                    holdCities.pop(destI)
                    src = currentdest
                if current < minPath:
                    minPath = current
                    bestPath = path
            return bestPath, minPath
        except:
            return None

    def centerPoint(self) -> (int, float):
        min_max_value = sys.maxsize
        index = 0
        g_algo = GraphAlgo(self.graph)
        g1 = MinHeapDijkstra.DijkstraUsingMinHeap.Graph(g_algo)
        try:
            for i in self.graph.nodes.keys():
                g1.dijkstra_GetMinDistances(i)
                if g1.max == sys.maxsize:
                    raise Exception()
                if g1.max < min_max_value:
                    min_max_value = g1.max
                    index = i
            ans = (index, min_max_value)
            return ans
        except:
            return (-1, inf)

    def plot_graph(self) -> None:
        self.test_py_game_1()

    def is_connected(self) -> bool:
        if (not self.bfs(self.graph)):
            return False
        try:
            reversed_graph: DiGraph = self.reverse(self.graph)
            if not self.bfs(reversed_graph):
                return False
            return True
        except:
            return False

    def bfs(self, graph: DiGraph) -> bool:
        flag = True
        for node in graph.nodes:  # first lets set tag of all nodes to 0 e.g not visited
            graph.nodes.get(node).tag = 0
        queue = Queue(maxsize=len(graph.nodes))
        # //get first node and run bfs from it
        for key in graph.nodes.keys():
            if not flag:
                break
            flag = False
            src: Node = graph.nodes.get(key)
            queue.put(key)
            src.tag = 1
        while (not queue.empty()):
            current_nodes_key = queue.get()
            neighbors = graph.all_out_edges_of_node(current_nodes_key)
            for neighbor_key in neighbors.keys():
                current_neighbor_node: Node = graph.nodes.get(neighbor_key)
                if current_neighbor_node.tag == 0:
                    current_neighbor_node.tag = 1
                    queue.put(neighbor_key)
        for node in graph.nodes:  # // if we find for some node that its tag is 0 e.g hasn't been visited then return false.
            if (graph.nodes.get(node).tag == 0):
                return False
        return True

    def reverse(self, graph: DiGraph) -> DiGraph:
        reversed_graph: DiGraph = DiGraph()
        for connected_key in graph.nodes.keys():  # //traverse through each node
            if not connected_key in reversed_graph.nodes:  # //only if graph dosent already have the node then add it
                src_bfr_reverse: Node = graph.nodes.get(connected_key)
                reversed_graph.nodes[connected_key] = src_bfr_reverse
            neighbors = graph.all_out_edges_of_node(connected_key)
            for neighbor_of_connected_key in neighbors.keys():  # //traverse through edges coming out of each node
                if not neighbor_of_connected_key in reversed_graph.nodes.keys():  # //only if graph dosent already have the node then add it
                    dst_bfr_reverse: Node = graph.nodes.get(neighbor_of_connected_key)
                    reversed_graph.nodes[neighbor_of_connected_key] = dst_bfr_reverse
                weight_of_reversed_edge = graph.nodes.get(neighbor_of_connected_key).inEdges.get(connected_key)
                reversed_graph.add_edge(neighbor_of_connected_key, connected_key, weight_of_reversed_edge)

        return reversed_graph

    def findpath(self, nodes: List[Node], graph: DiGraph) -> bool:
        copy_graph = GraphAlgo(copy.deepcopy(graph))
        flag1 = True
        try:
            keys = []
            for nodeiter in graph.nodes:
                keys.append(nodeiter)
            src_node = False
            src_node_key = 0
            for nodeiter2 in copy_graph.graph.nodes:
                if not flag1:
                    break
                if copy_graph.graph.nodes[nodeiter2] in nodes:
                    src_node_key = nodeiter2
                    src_node = True
                flag1 = False
            if src_node:
                copy_graph.is_connected()
                flag1 = True
                for i in keys:
                    if (i != src_node_key) and (graph.nodes.get(i).tag != 1) and (i in keys):
                        return False
            copy_graph.is_connected()
            for i in range(len(keys)):
                key_current = keys[i]
                if (key_current != src_node_key) and (key_current in nodes) and (graph.nodes.get(key_current).tag != 1):
                    return False

            return True
        except:
            return False



    def test_py_game_1(self, ):
        pygame.init()
        scr = pygame.display.set_mode((900, 650))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            scr.fill((255, 255, 255))
            scaling = ()
            self.graph.set_location()
            scaling = self.graph.caclulate_minmax()
            min_x = scaling[0][0]
            min_y = scaling[0][1]
            lon = scaling[2][0]
            lat = scaling[2][1]
            color = (200, 30, 70)
            font = pygame.font.SysFont('comicsans', 12)
            for node in self.graph.nodes:
                for edge in self.graph.all_out_edges_of_node(node):
                    x1 = (self.graph.nodes[node].geolocation[0]-min_x)*(lon) + 60
                    y1 = (self.graph.nodes[node].geolocation[1]-min_y)*(lat) + 60
                    x2 = (self.graph.nodes[edge].geolocation[0] - min_x) * (lon) + 60
                    y2 = (self.graph.nodes[edge].geolocation[1] - min_y) * (lat) + 60
                    pygame.draw.line(scr, color, (x1, y1), (x2, y2), 2)
            for node in self.graph.nodes:
                for edge in self.graph.all_out_edges_of_node(node):
                    x1 = (self.graph.nodes[node].geolocation[0]-min_x)*(lon) + 60
                    y1 = (self.graph.nodes[node].geolocation[1]-min_y)*(lat) + 60
                    x2 = (self.graph.nodes[edge].geolocation[0] - min_x) * (lon) + 60
                    y2 = (self.graph.nodes[edge].geolocation[1] - min_y) * (lat) + 60
                    self.drawArrowLine(scr, x1, y1, x2, y2, 6, 5)
            for node in self.graph.nodes:
                x = (self.graph.nodes[node].geolocation[0] - min_x) * (lon) + 60
                y = (self.graph.nodes[node].geolocation[1] - min_y) * (lat) + 60
                pygame.draw.circle(scr, (0, 0, 0), (x, y), 4)
                txt= font.render(str(node) ,1 , (0, 0, 0))
                scr.blit(txt, (x-8, y-19))

            pygame.display.flip()
        pygame.quit()


    def drawArrowLine(self, scr: pygame.Surface, x1, y1, x2, y2, d, h):
        dx = x2 - x1
        dy = y2 - y1
        D = math.sqrt(dx * dx + dy * dy)
        xm = D - 3.5
        xn = xm
        ym = h
        yn = (0 - h)
        sin = dy / D
        cos = dx / D
        x = xm * cos - ym * sin + x1
        ym = xm * sin + ym * cos + y1
        xm = x
        x = xn * cos - yn * sin + x1
        yn = xn * sin + yn * cos + y1
        xn = x
        newX2 = (xm + xn) / 2
        newY2 = (ym + yn) / 2
        dx1 = newX2 - x1
        dy1 = newY2 - y1
        D1 = math.sqrt(dx1 * dx1 + dy1 * dy1)
        xm1 = D1 - d
        xn1 = xm1
        ym1 = h
        yn1 = 0 - h
        sin1 = dy1 / D1
        cos1 = dx1 / D1
        nx = xm1 * cos1 - ym1 * sin1 + x1
        ym1 = xm1 * sin1 + ym1 * cos1 + y1
        xm1 = nx
        nx = xn1 * cos1 - yn1 * sin1 + x1
        yn1 = xn1 * sin1 + yn1 * cos1 + y1
        xn1 = nx
        points = [(newX2, newY2), (xm1, ym1), (xn1, yn1)]
        pygame.draw.polygon(scr, (200, 30, 70), points)
