from typing import Dict, Tuple

from pydantic.env_settings import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo: Dict[Tuple[int, int], int] = dict()

        return self.dp_top_down(piles, 0, len(piles) // 2, memo) > 0

    def dp_top_down(self, piles: List[int], index: int, left_choose: int, memo: Dict[Tuple[int, int], int]) -> int:

        if index == len(piles) and left_choose > 0:
            return float("-inf")

        if index == len(piles):
            return 0

        if (index, left_choose) in memo:
            return memo[index, left_choose]

        result = max(
            self.dp_top_down(piles, index + 1, left_choose, memo) - piles[index],
            self.dp_top_down(piles, index + 1, left_choose - 1, memo) + piles[index]
        )

        memo[index, left_choose] = result

        return result