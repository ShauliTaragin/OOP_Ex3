import sys
from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from MinHeapDijkstra import DijkstraUsingMinHeap


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        g_algo.graph.add_node(17,(35.62364,34.346164,0))
        g_algo.graph.add_node(14,(32.62364,33.346164,0))
        g_algo.graph.add_edge(14, 17, 4.1251)
        self.assertEqual(True, g_algo.save_to_json("../data/b1.json"))
        self.assertEqual( 17 ,g_algo.graph.nodes.get(17).key)
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json("../data/b1.json")
        self.assertEqual(17 ,g_algo2.graph.nodes.get(17).key)

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
        # g_algo = GraphAlgo(g2)
        # g1=MinHeapDijkstra.DijkstraUsingMinHeap.Graph(g_algo)
        # g1.dijkstra_GetMinDistances(0)
        max1=sys.maxsize
        index=0
        g_algo = GraphAlgo(g2)
        g1 = DijkstraUsingMinHeap.Graph(g_algo)
        for i in g2.nodes.keys():
            g1.dijkstra_GetMinDistances(i)
            if(g1.max<max1):
                max1 = g1.max
                index = i
        print(index)
        print(max1)
    def test_tsp(self):
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
        self.assertEqual(([1, 2, 3, 4], 4.5),g_algo.TSP([1, 2, 4]))
        g2 = DiGraph("../data/A0.json")
        g_algo.graph = g2
        self.assertEqual(([10, 0, 1, 2, 3, 4], 6.914963541041983), g_algo.TSP([1,2,4,10]))
        g3 = DiGraph("../data/A1.json")
        g_algo.graph = g3
        self.assertEqual(([10, 9, 8, 7, 6, 5, 6, 2, 1, 0], 14.947567898812181), g_algo.TSP([0,5,7,9,10]))
        self.assertIsNone( g_algo.TSP([0,5,7,9,100]))
    def test_center_point(self):
        g2 = DiGraph("../data/G3.json")
        g_algo=GraphAlgo(g2)
        print(g_algo.centerPoint())
    def test_plot_graph(self):
        self.fail()
