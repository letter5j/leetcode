from typing import List, Dict, Tuple


class Solution:
    def change_top_down(self, amount: int, coins: List[int]) -> int:

        memo: Dict[Tuple[int, int], bool] = dict()

        return self.dp_top_down(coins, len(coins) - 1, amount, memo)

    def dp_top_down(self, coins: List[int], index: int, amount: int, memo: Dict[Tuple[int, int], int]) -> int:

        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if index < 0:
            return 0
        if (index, amount) in memo:
            return memo[index, amount]
        if coins[index] > amount:
            result = self.dp_top_down(coins, index - 1, amount, memo)
        else:
            result = self.dp_top_down(coins, index - 1, amount, memo) + \
                     self.dp_top_down(coins, index, amount - coins[index], memo)

        memo[index, amount] = result
        return result
