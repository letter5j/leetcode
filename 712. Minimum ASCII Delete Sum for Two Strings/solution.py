from typing import Dict, Tuple, List


class Solution:
    def minDistance_bottom_up(self, s1: str, s2: str) -> int:

        s1_length = len(s1)
        s2_length = len(s2)

        dp: List[List[int]] = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]

        for row in range(1, s1_length + 1):
            dp[row][0] = ord(s1[row - 1]) + dp[row - 1][0]
        for column in range(1, s2_length + 1):
            dp[0][column] = ord(s2[column - 1]) + dp[0][column - 1]

        for row in range(1, s1_length + 1):
            for column in range(1, s2_length + 1):
                if s1[row - 1] == s2[column - 1]:
                    dp[row][column] = dp[row - 1][column - 1]
                else:
                    dp[row][column] = min(
                        dp[row - 1][column] + ord(s1[row - 1]),
                        dp[row][column - 1] + ord(s2[column - 1])
                    )

        return dp[s1_length][s2_length]
