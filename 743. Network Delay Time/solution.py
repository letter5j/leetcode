import functools
from typing import Optional, Dict, Set, List, Tuple, Any
from queue import PriorityQueue


@functools.total_ordering
class NodeInfo:
    index: int
    distance_from_start: int

    def __init__(self, index: int, distance_from_start: int):
        self.index = index
        self.distance_from_start = distance_from_start

    def __gt__(self, other: Any):
        return self.distance_from_start < other.distance_from_start

    def __eq__(self, other: Any):
        return self.index == other.index and self.distance_from_start == other.distance_from_start


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjacency_list: List[List[Tuple[int, int]]] = self.build_adjacency_list(times, n)

        destination_from_start: List[int] = self.dijkstra(adjacency_list, k)

        max_distance = max(destination_from_start[1:])
        return -1 if float('inf') == max_distance else max_distance

    def build_adjacency_list(self, times: List[List[int]], n: int) -> List[List[Tuple[int, int]]]:
        adjacency_list: List[List[Tuple[int, int]]] = list()
        for i in range(n + 1):
            adjacency_list.append(list())

        for time in times:
            from_node: int = time[0]
            to_node: int = time[1]
            weight: int = time[2]
            connection: Tuple[int, int] = (to_node, weight)
            adjacency_list[from_node].append(connection)
        return adjacency_list

    def dijkstra(self, graph: List[List[Tuple[int, int]]], start_node: int) -> List[int]:

        node_count: int = len(graph)

        destination_from_start: List[int] = [float('inf')] * node_count

        destination_from_start[start_node] = 0

        priority_queue: PriorityQueue = PriorityQueue()
        priority_queue.put(NodeInfo(start_node, 0))

        while priority_queue.qsize() != 0:
            current_node: NodeInfo = priority_queue.get()
            current_index = current_node.index
            current_distance = current_node.distance_from_start

            if current_distance > destination_from_start[current_index]:
                continue

            for next_node_index, next_node_weight in graph[current_index]:
                next_node_distance = current_distance + next_node_weight
                if next_node_distance < destination_from_start[next_node_index]:
                    destination_from_start[next_node_index] = next_node_distance
                    priority_queue.put(NodeInfo(next_node_index, next_node_distance))

        return destination_from_start
