import functools
from queue import PriorityQueue
from typing import List, Tuple, Any


@functools.total_ordering
class NodeInfo:
    index: int
    min_from_start: int

    def __init__(self, index: int, max_from_start: int):
        self.index = index
        self.min_from_start = max_from_start

    def __gt__(self, other: Any):
        return self.min_from_start > other.min_from_start

    def __eq__(self, other: Any):
        return self.index == other.index and self.min_from_start == other.min_from_start


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        return self.dijkstra(heights)

    def get_index(self, graph: List[List[int]], row: int, column: int) -> int:
        column_len: int = len(graph[0])
        return column_len * row + column

    def get_row_column(self, graph: List[List[int]], index: int) -> Tuple[int, int]:
        column_len: int = len(graph[0])
        return index // column_len, index % column_len

    def dijkstra(self, graph: List[List[int]]) -> int:

        row_len: int = len(graph)
        column_len: int = len(graph[0])
        min_from_start: List[int] = [float('inf')] * (row_len * column_len)

        min_from_start[0] = 0

        priority_queue: PriorityQueue = PriorityQueue()
        priority_queue.put(NodeInfo(0, 0))

        while priority_queue.qsize() != 0:
            current_node: NodeInfo = priority_queue.get()
            current_index = current_node.index
            current_min_different = current_node.min_from_start

            current_row, current_column = self.get_row_column(graph, current_index)

            if current_index == self.get_index(graph, row_len - 1, column_len - 1):
                return current_min_different

            if current_min_different > min_from_start[current_index]:
                continue
            next_node: List[Tuple[int, int]] = [(current_row - 1, current_column), (current_row + 1, current_column),
                                                (current_row, current_column - 1), (current_row, current_column + 1)]
            for next_node_row, next_node_column in next_node:
                if next_node_row < 0 or next_node_row >= row_len or next_node_column < 0 or next_node_column >= column_len:
                    continue
                next_node_index = self.get_index(graph, next_node_row, next_node_column)
                next_node_min_different: int = min(min_from_start[next_node_index], max(current_min_different, abs(
                    graph[next_node_row][next_node_column] - graph[current_row][current_column])))
                if next_node_min_different < min_from_start[next_node_index]:
                    min_from_start[next_node_index] = next_node_min_different
                    priority_queue.put(NodeInfo(next_node_index, next_node_min_different))

        return min_from_start[-1]
