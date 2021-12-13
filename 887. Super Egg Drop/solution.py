from typing import Dict, List, Tuple


class Solution:
    def superEggDrop_top_down(self, k: int, n: int) -> int:
        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp_top_down(k, n, memo)

    def dp_top_down(self, k: int, n: int, memo: Dict[Tuple[int, int], int]) -> int:

        if n == 0:
            return 0
        if k == 1:
            return n

        if (k, n) in memo:
            return memo[k, n]

        result = float("inf")
        for i in range(1, n + 1):
            result = min(result, max(self.dp_top_down(k - 1, i - 1, memo), self.dp_top_down(k, n - i, memo)) + 1)
        memo[k, n] = result

        return result