import functools
from typing import Optional, Dict, Set, List, Tuple, Any
from queue import PriorityQueue


@functools.total_ordering
class NodeInfo:
    index: int
    success_from_start: float

    def __init__(self, index: int, success_from_start: float):
        self.index = index
        self.success_from_start = success_from_start

    def __gt__(self, other: Any):
        return self.success_from_start < other.success_from_start

    def __eq__(self, other: Any):
        return self.index == other.index and self.success_from_start == other.success_from_start


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjacency_list: List[List[Tuple[int, float]]] = self.build_adjacency_list(edges, succProb, n)

        result: float = self.dijkstra(adjacency_list, start, end)
        return 0 if float("-inf") == result else result

    def build_adjacency_list(self, edges: List[List[int]], succ_prob: List[float], n: int) -> List[
        List[Tuple[int, float]]]:
        adjacency_list: List[List[Tuple[int, float]]] = list()
        for i in range(n):
            adjacency_list.append(list())
        for index, edge in enumerate(edges):
            edge_1 = edge[0]
            edge_2 = edge[1]
            probability: float = succ_prob[index]
            adjacency_list[edge_1].append((edge_2, probability))
            adjacency_list[edge_2].append((edge_1, probability))

        return adjacency_list

    def dijkstra(self, graph: List[List[Tuple[int, float]]], start_node: int, end_node) -> float:

        node_count: int = len(graph)

        success_from_start: List[float] = [float('-inf')] * node_count

        success_from_start[start_node] = 0

        priority_queue: PriorityQueue = PriorityQueue()
        priority_queue.put(NodeInfo(start_node, 1))

        while priority_queue.qsize() != 0:
            current_node: NodeInfo = priority_queue.get()
            current_index = current_node.index
            current_success = current_node.success_from_start

            if current_index == end_node:
                return current_success

            if current_success < success_from_start[current_index]:
                continue

            for next_node_index, next_node_weight in graph[current_index]:
                next_node_success: float = current_success * next_node_weight
                if next_node_success > success_from_start[next_node_index]:
                    success_from_start[next_node_index] = next_node_success
                    priority_queue.put(NodeInfo(next_node_index, next_node_success))

        return success_from_start[end_node]
