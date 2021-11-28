from typing import List


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
