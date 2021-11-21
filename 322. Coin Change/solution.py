from typing import List, Dict


class Solution:
    # dp1 bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp: List[int] = [float("inf")] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount + 1, 1):

            for coin in coins:
                if (i - coin) < 0:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[amount] if dp[amount] != float("inf") else -1

    # dp2 top-down
    def coin_change(self, coins: List[int], amount: int) -> int:
        memo: Dict[int, int] = dict()

        return self.dp(coins, amount, memo)

    def dp(self, coins: List[int], amount: int, memo: Dict[int, int]) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]

        result = float("inf")
        for coin in coins:

            sub_result = self.dp(coins, amount - coin, memo)

            if sub_result == -1:
                continue
            result = min(result, sub_result + 1)
        memo[amount] = result if result != float("inf") else -1
        return memo[amount]
