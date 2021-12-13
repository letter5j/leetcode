from typing import Dict, List, Tuple


class Solution:
    def superEggDrop_top_down(self, k: int, n: int) -> int:
        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp_top_down_binary_search(k, n, memo)

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

    def dp_top_down_binary_search(self, k: int, n: int, memo: Dict[Tuple[int, int], int]) -> int:

        if n == 0:
            return 0
        if k == 1:
            return n

        if (k, n) in memo:
            return memo[k, n]

        result = float("inf")

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            broken = self.dp_top_down_binary_search(k - 1, mid - 1, memo)
            not_broken = self.dp_top_down_binary_search(k, n - mid, memo)
            if broken > not_broken:
                right = mid - 1
                result = min(result, broken + 1)
            else:
                left = mid + 1
                result = min(result, not_broken + 1)

        memo[k, n] = result

        return result
