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

    def change_bottom_up(self, amount: int, coins: List[int]) -> int:
        coin_length = len(coins)
        dp: List[List[int]] = [[0] * (amount + 1) for _ in range(coin_length + 1)]

        for coin in range(1, coin_length + 1):
            dp[coin][0] = 1

        for coin in range(1, coin_length + 1):
            for sub_amount in range(1, amount + 1):

                if coins[coin - 1] > sub_amount:
                    dp[coin][sub_amount] = dp[coin - 1][sub_amount]
                else:
                    dp[coin][sub_amount] = dp[coin - 1][sub_amount] + \
                                           dp[coin][sub_amount - coins[coin - 1]]

        return dp[coin_length][amount]

    def change_bottom_up_compress(self, amount: int, coins: List[int]) -> int:
        coin_length = len(coins)
        dp: List[int] = [0] * (amount + 1)
        dp[0] = 1
        for coin in range(coin_length):
            for sub_amount in range(1, amount + 1):
                if sub_amount >= coins[coin]:
                    dp[sub_amount] = dp[sub_amount] + dp[sub_amount - coins[coin]]

        return dp[amount]
