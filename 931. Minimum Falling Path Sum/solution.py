from typing import List, Dict, Tuple


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        min_path = float("inf")
        memo: Dict[Tuple[int, int], int] = dict()
        for column in range(len(matrix[0])):
            min_path = min(min_path, self.top_down_dp(matrix, len(matrix) - 1, column, memo))
        return min_path

    def top_down_dp(self, matrix: List[List[int]], row: int, column: int, memo: Dict[Tuple[int, int], int]) -> int:

        if column < 0 or column >= len(matrix[0]):
            return float("inf")
        if row < 0 or row >= len(matrix):
            return float("inf")

        if (row, column) in memo:
            return memo[(row, column)]

        result = min(
            self.top_down_dp(matrix, row - 1, column - 1, memo),
            self.top_down_dp(matrix, row - 1, column, memo),
            self.top_down_dp(matrix, row - 1, column + 1, memo)
        )
        result = (result if result != float("inf") else 0) + matrix[row][column]

        memo[(row, column)] = result
        return result

a = Solution()

a.minFallingPathSum(
[[2,1,3],[6,5,4],[7,8,9]]
)
