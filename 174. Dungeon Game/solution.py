from typing import List, Dict, Tuple


class Solution:
    def calculateMinimumHP_top_down(self, dungeon: List[List[int]]) -> int:
        memo: Dict[Tuple[int, int], int] = dict()

        return self.dp_top_down(dungeon, 0, 0, memo)

    def dp_top_down(self, dungeon: List[List[int]], row_index: int, column_index: int,
                    memo: Dict[Tuple[int, int], int]) -> int:

        if row_index >= len(dungeon) or column_index >= len(dungeon[0]):
            return float("inf")

        if row_index == len(dungeon) - 1 and column_index == len(dungeon[0]) - 1:
            return 1 if dungeon[row_index][column_index] > 0 else abs(dungeon[row_index][column_index]) + 1

        if (row_index, column_index) in memo:
            return memo[row_index, column_index]

        result = min(self.dp_top_down(dungeon, row_index + 1, column_index, memo),
                     self.dp_top_down(dungeon, row_index, column_index + 1, memo)) - dungeon[row_index][
                     column_index]
        if result <= 0:
            result = 1
        memo[row_index, column_index] = result
        return result

    def calculateMinimumHP_bottom_up(self, dungeon: List[List[int]]) -> int:

        row_length = len(dungeon)
        column_length = len(dungeon[0])
        dp: List[List[int]] = [[float("inf")] * (column_length) for _ in range(row_length)]
        for row_index in range(row_length - 1, -1, -1):
            for column_index in range(column_length - 1, -1, -1):
                if (row_index == row_length - 1) and (column_index == column_length - 1):
                    dp[row_index][column_index] = 1 if dungeon[row_index][column_index] > 0 else abs(
                        dungeon[row_index][column_index]) + 1
                else:
                    dp[row_index][column_index] = min(
                        dp[row_index + 1][column_index] if row_index < row_length - 1 else float("inf"),
                        dp[row_index][column_index + 1] if column_index < column_length - 1 else float("inf")) - \
                                                  dungeon[row_index][
                                                      column_index]
                    if dp[row_index][column_index] <= 0:
                        dp[row_index][column_index] = 1

        return dp[0][0]

    def calculateMinimumHP_bottom_up_compress(self, dungeon: List[List[int]]) -> int:

        row_length = len(dungeon)
        column_length = len(dungeon[0])
        dp: List[int] = [float("inf")] * column_length
        prev: List[int] = [float("inf")] * column_length

        for row_index in range(row_length - 1, -1, -1):

            for column_index in range(column_length - 1, -1, -1):
                if (row_index == row_length - 1) and (column_index == column_length - 1):
                    dp[column_index] = 1 if dungeon[row_index][column_index] > 0 else abs(
                        dungeon[row_index][column_index]) + 1
                else:
                    dp[column_index] = min(prev[column_index],
                                           dp[column_index + 1] if column_index < column_length - 1 else float("inf")) - \
                                       dungeon[row_index][column_index]
                    if dp[column_index] <= 0:
                        dp[column_index] = 1
                prev[column_index] = dp[column_index]
        return dp[0]
