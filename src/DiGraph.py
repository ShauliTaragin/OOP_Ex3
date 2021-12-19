from GraphInterface import GraphInterface
from Node import Node
import json


class DiGraph(GraphInterface):

    def __init__(self, jsonfile: str = None):
        self._nodes = {}
        self._numOfEdges = 0
        self._mc = 0
        if jsonfile is not None:
            with open(jsonfile,'r') as jsonFile:
                json_object = json.load(jsonFile)
                jsonFile.close()
            edges_json = json_object['Edges']
            nodes_json = json_object['Nodes']
            for nodeIter in nodes_json:
                location=str(nodeIter['pos']).split(',')
                pos_tuple = (float(location[0]), float(location[1]), float(location[2]))
                self.add_node(nodeIter['id'], pos_tuple)
            for edgeIter in edges_json:
                src = edgeIter['src']
                weight = edgeIter['w']
                dest = edgeIter['dest']
                self.add_edge(src, dest, weight)

    def v_size(self) -> int:
        return len(self._nodes)
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """

    def e_size(self) -> int:
        return self._numOfEdges
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """

    def get_all_v(self) -> dict:
        return self._nodes
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 not in self._nodes:
            return {}
        return self._nodes[id1].inEdges

    """return a dictionary of all the nodes connected to (into) node_id ,
                    each node is represented using a pair (other_node_id, weight)
                     """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 not in self._nodes:
            return {}
        return self._nodes[id1].outEdges
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

    def get_mc(self) -> int:
        return self._mc
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        node_src = self._nodes.get(id1)
        node_dst = self._nodes.get(id2)
        if (node_src or node_dst or node_src.outEdges[id2]) is None:
            return False
        else:
            node_src.outEdges[id2] = weight
            node_dst.inEdges[id1] = weight
            self._mc += 1
            self._numOfEdges += 1
            return True

        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        node_src = self._nodes.get(node_id)
        if node_src is not None:
            return False
        else:
            node_src = Node(node_id, pos)
            self._nodes[node_id] = node_src
            self._mc += 1
            return True
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

    def remove_node(self, node_id: int) -> bool:
        if self._nodes.get(node_id) is None:
            return False
        else:
            self._nodes.pop(node_id)
            self._mc += 1
            return True

        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        node = self._nodes.get(node_id1)
        node2 = self._nodes.get(node_id2)
        if (node or node2) is None:
            return False
        else:
            node.outEdges.pop(node_id2)
            node2.inEdges.pop(node_id1)
            self._mc += 1
            self._numOfEdges -= 1
            return True

        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
    def __repr__(self):
        return "Graph: |V|={} , |E|={}".format(len(self._nodes),self._numOfEdges)