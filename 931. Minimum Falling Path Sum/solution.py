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

    def minFallingPathSum_bottom_up(self, matrix: List[List[int]]) -> int:

        row_length = len(matrix)
        column_length = len(matrix[0])

        dp: List[List[int]] = list()
        for row in range(row_length + 2):
            dp.append([float("inf")] * (column_length + 2))
        min_path = float("inf")
        for row in range(1, row_length + 1, 1):
            for column in range(1, column_length + 1, 1):
                result = min(
                    dp[row - 1][column - 1],
                    dp[row - 1][column],
                    dp[row - 1][column + 1]
                )
                dp[row][column] = (result if result != float("inf") else 0) + matrix[row - 1][column - 1]
                if row == row_length:
                    if dp[row][column] < min_path:
                        min_path = dp[row][column]
        return min_path
