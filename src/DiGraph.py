from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self, jsonfile: str):
        self._nodes = {}
        self._numOfEdges = 0
        self._mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

    def all_in_edges_of_node(self, id1: int) -> dict:
        node = Node(self._nodes.get(id1))
        ans_dict = {}
        for x in node.inEdges.keys():
            node_temp = Node(self._nodes.get(x))
            ans_dict[x] = node_temp.weight
        return ans_dict
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        node = Node(self._nodes.get(id1))
        ans_dict = {}
        for x in node.outEdges.keys():
            node_temp = Node(self._nodes.get(x))
            ans_dict[x] = node_temp.weight
        return ans_dict
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
        node_src = Node(self._nodes.get(id1))
        nodeDst = Node(self._nodes.get(id2))
        if (node_src or nodeDst or node_src.outEdges[id2]) is None:
            return False
        else:
            node_src.outEdges[id2] = weight
            nodeDst.inEdges[id1] = weight
            self._mc += 1
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
        node_src = Node(self._nodes.get(node_id))
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
        node = Node(self._nodes.get(node_id1))
        node2 = Node(self._nodes.get(node_id2))
        if (node or node2) is None:
            return False
        else:
            node.outEdges.pop(node_id2)
            node2.inEdges.pop(node_id1)
            self._mc += 1
            return True

        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
