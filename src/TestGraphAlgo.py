import sys
from unittest import TestCase

import MinHeapDijkstra
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 4, 5)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(1, 3, 1.9)
        g.add_edge(2, 3, 1.1)
        g.add_edge(3, 4, 2.1)
        g.add_edge(4, 2, .5)
        g_algo = GraphAlgo(g)
        g_algo.save_to_json("../data/tester.json")
        g_algo.graph=None
        g_algo.load_from_json("../data/tester.json")
        self.assertEqual("fasf", g_algo.get_graph().get_all_v().__str__())

    def test_shortest_path(self):
        g2 = DiGraph("../data/1000Nodes.json")
        # g = DiGraph()  # creates an empty directed graph
        # for n in range(4):
        #     g.add_node(n)
        # g.add_edge(0, 1, 1)
        # g.add_edge(1, 0, 1.1)
        # g.add_edge(1, 2, 1.3)
        # g.add_edge(2, 3, 1.1)
        # g.add_edge(1, 3, 1.9)
        # g.remove_edge(1, 3)
        # g.add_edge(1, 3, 10)
        g_algo = GraphAlgo(g2)
        g1=MinHeapDijkstra.DijkstraUsingMinHeap.Graph(g_algo)
        g1.dijkstra_GetMinDistances(0)
        max1=sys.maxsize
        index=0
        g_algo = GraphAlgo(g2)
        g1 = MinHeapDijkstra.DijkstraUsingMinHeap.Graph(g_algo)
        for i in g2.nodes.keys():
            g1.dijkstra_GetMinDistances(i)
            if(g1.max<max1):
                max1 = g1.max
                index = i
        print (index)
        print(max1)
    def test_tsp(self):
        self.fail()
    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
