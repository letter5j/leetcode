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

