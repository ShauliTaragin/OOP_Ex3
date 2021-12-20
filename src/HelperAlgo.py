from queue import Queue

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node import Node


def bfs(graph: DiGraph) -> bool:
    flag = True
    for node in graph.nodes:# first lets set tag of all nodes to 0 e.g not visited
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
    for node in graph.nodes:#// if we find for some node that its tag is 0 e.g hasn't been visited then return false.
        if (graph.nodes.get(node).tag == 0):
            return False
    return True

def reverse(graph: DiGraph) -> DiGraph:
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
def findpath(nodes: list[Node], graph: DiGraph) -> bool:
    copy_graph = GraphAlgo(graph)
    # copy_graph = copy.deepcopy(graph)
    flag1 = True
    try:
        keys = []
        for nodeiter in graph.nodes:
            nodeiter: Node
            keys.append(nodeiter.key)
        src_node = False
        src_node_key = 0
        for nodeiter2 in copy_graph.graph.nodes:
            if not flag1:
                break
            nodeiter2: Node
            if nodeiter2 in nodes:
                src_node_key = nodeiter2.key
                src_node = True
            flag1 = False
        if src_node:
            copy_graph.isConnected()
            flag1 = True
            for i in keys:
                if (i != src_node_key) and (graph.nodes.get(i).tag != 1) and (i in keys):
                    return False
        copy_graph.isConnected()
        for i in range(len(keys)):
            key_current = keys[i]
            if (key_current != src_node_key) and (key_current in nodes) and (graph.nodes.get(key_current).tag != 1):
                return False

        return True
    except:
        return False