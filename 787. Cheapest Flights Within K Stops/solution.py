from typing import Dict, List, Tuple


class Solution:
    def findCheapestPrice_top_down(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency_matrix = self.get_adjacency_matrix(n, flights)
        memo: Dict[Tuple[int, int], int] = dict()
        result = self.dp_top_down(adjacency_matrix, src, dst, k, 0, memo)
        return result if result != float("inf") else -1

    def dp_top_down(self, adjacency_matrix: List[List[int]], src: int, dst: int, k: int, passed_k: int,
                    memo: Dict[Tuple[int, int], int]):
        if passed_k == k:
            return adjacency_matrix[src][dst]
        if src == dst:
            return 0
        if (src, passed_k) in memo:
            return memo[src, passed_k]

        result = adjacency_matrix[src][dst]

        for dst_index, cost in enumerate(adjacency_matrix[src]):
            result = min(result, self.dp_top_down(adjacency_matrix, dst_index, dst, k, passed_k + 1, memo) + cost)

        memo[src, passed_k] = result
        return result

    def get_adjacency_matrix(self, n: int, flights: List[List[int]]) -> List[List[int]]:
        adjacency_matrix = [[float("inf")] * n for _ in range(n)]
        flight: List[int]
        for flight in flights:
            src = flight[0]
            dest = flight[1]
            cost = flight[2]
            adjacency_matrix[src][dest] = cost
        return adjacency_matrix
