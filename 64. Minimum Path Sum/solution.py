from typing import List, Dict, Tuple


class Solution:

    def minPathSum_top_down(self, grid: List[List[int]]) -> int:

        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp_top_down(grid, len(grid) - 1, len(grid[0]) - 1, memo)

    def dp_top_down(self, grid: List[List[int]], row: int, column: int, memo: Dict[Tuple[int, int], int]) -> int:
        if row == 0 and column == 0:
            return grid[0][0]
        if row < 0:
            return float("inf")
        if column < 0:
            return float("inf")
        if (row, column) in memo:
            return memo[row, column]
        result = min(self.dp_top_down(grid, row - 1, column, memo),
                     self.dp_top_down(grid, row, column - 1, memo)) + grid[row][column]
        memo[row, column] = result
        return result

    def minPathSum_bottom_up(self, grid: List[List[int]]) -> int:
        row_length = len(grid)
        column_length = len(grid[0])
        dp: List[List[int]] = [[0] * column_length for _ in range(row_length)]

        for row in range(row_length):
            for column in range(column_length):
                dp[row][column] = (min(
                    dp[row - 1][column] if row > 0 else float("inf"),
                    dp[row][column - 1] if column > 0 else float("inf")) if row > 0 or column > 0 else 0) + \
                                  grid[row][column]

        return dp[-1][-1]

    def minPathSum_bottom_up_compress(self, grid: List[List[int]]) -> int:
        row_length = len(grid)
        column_length = len(grid[0])
        dp: List[int] = [0] * column_length
        dp[0] = grid[0][0]
        for row in range(row_length):
            for column in range(column_length):
                dp[column] = (min(
                    dp[column] if row > 0 else float("inf"),
                    dp[column - 1] if column > 0 else float("inf")) if row > 0 or column > 0 else 0) + \
                             grid[row][column]

        return dp[column_length - 1]
