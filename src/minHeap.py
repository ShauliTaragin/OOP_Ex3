import sys

from src.DiGraph import DiGraph
from src.Node import Node


class MinHeap:
    def __init__(self, capacity: int, key: int, graph: DiGraph):
        self.node_holder = {}
        self.index_of_nodes = {}
        # //init the src as the min node in the heap with weight 0
        node_temp: Node = (graph.nodes.get(key))
        node_temp.weight = 0
        self.node_holder[0] = node_temp
        self.heap_size = 0

    # //insert the node to the heap
    def insert(self, node: Node):
        self.heap_size += 1
        idx = self.heap_size
        node.weight = sys.maxsize
        self.node_holder[idx] = node
        self.index_of_nodes[node.key] = idx
        # // put the node at the current index at his place in the heap
        self.heapfyUp(idx)

    # // simple heapfyUp
    def heapfyUp(self, pos: int):
        parentIdx = int(pos / 2)
        currentIdx = pos
        parent_node: Node = self.node_holder.get(parentIdx)
        current_node: Node = self.node_holder.get(currentIdx)
        while (currentIdx > 0 and parent_node.weight > current_node.weight):
            parent_node: Node = self.node_holder.get(parentIdx)
            current_node: Node = self.node_holder.get(currentIdx)
            # //swap the positions
            self.index_of_nodes[current_node.key] = parentIdx
            self.index_of_nodes[parent_node.key] = currentIdx
            self.swap(currentIdx, parentIdx)
            currentIdx = parentIdx
            parentIdx = int(parentIdx / 2)

    # // get the node with the minimum weight
    def extractMin(self) -> Node:
        min: Node = self.node_holder.get(0)
        lastNode: Node = self.node_holder.get(self.heap_size)
        # // update the indexes[] and move the last node to the top
        self.index_of_nodes[lastNode.key] = 0
        self.node_holder[0] = lastNode
        self.node_holder[self.heap_size] = None
        self.sinkDown(0)
        self.heap_size -= 1
        return min

    # // push the node at the current index down
    def sinkDown(self, k: int):
        smallest = k
        leftChildIdx = 2 * k
        rightChildIdx = 2 * k + 1
        smallest_node: Node = self.node_holder.get(smallest)
        left_child_node: Node = self.node_holder.get(leftChildIdx)
        right_child_node: Node = self.node_holder.get(rightChildIdx)
        if (leftChildIdx < self.heap_size and smallest_node.weight > left_child_node.weight):
            smallest = leftChildIdx
            smallest_node: Node = self.node_holder.get(left_child_node)
        if (rightChildIdx < self.heap_size and smallest_node.weight > right_child_node.weight):
            smallest = rightChildIdx
            smallest_node: Node = self.node_holder.get(left_child_node)
        if (smallest != k):
            smallestNode: Node = self.node_holder[smallest]
            kNode: Node = self.node_holder[k]
            # //swap the positions
            self.index_of_nodes[smallestNode.key] = k
            self.index_of_nodes[kNode.key] = smallest
            self.swap(k, smallest)
            self.sinkDown(smallest)

    # //swap the two nodes
    def swap(self, a: int, b: int):
        temp: Node = self.node_holder[a]
        self.node_holder[a] = self.node_holder[b]
        self.node_holder[b] = temp

    # //check if the heap is empty
    def isEmpty(self) -> bool:
        return self.heap_size == 0

    # //return the heapSize
    def heapSize(self) -> int:
        return self.heap_size
