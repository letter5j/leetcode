from typing import List, Dict, Tuple


class Solution:
    def longestPalindromeSubseq_bottom_up(self, s: str) -> int:

        s_length = len(s)

        dp: List[List[int]] = [[0] * s_length for _ in range(s_length)]

        for i in range(s_length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, s_length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][s_length - 1]

    def longestPalindromeSubseq_top_down(self, s: str) -> int:
        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp_top_down(s, 0, len(s) - 1, memo)

    def dp_top_down(self, s: str, start_index: int, end_index: int, memo: Dict[Tuple[int, int], int]) -> int:

        if start_index == end_index:
            return 1
        if start_index > end_index:
            return 0
        if (start_index, end_index) in memo:
            return memo[start_index, end_index]

        if s[start_index] == s[end_index]:
            result = self.dp_top_down(s, start_index + 1, end_index - 1, memo) + 2
        else:
            result = max(self.dp_top_down(s, start_index + 1, end_index, memo),
                         self.dp_top_down(s, start_index, end_index - 1, memo))
        memo[start_index, end_index] = result

        return result
