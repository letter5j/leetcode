from typing import Dict, Tuple, List


class Solution:
    def minimumDeleteSum_bottom_up(self, s1: str, s2: str) -> int:

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

    def minimumDeleteSum_top_down(self, s1: str, s2: str) -> int:
        memo: Dict[Tuple[int, int], int] = dict()

        result = self.dp_top_down(s1, s2, len(s1) - 1, len(s2) - 1, memo)
        return result

    def dp_top_down(self, s1: str, s2: str, index1: int, index2: int, memo: Dict[Tuple[int, int], int]) -> int:

        if index1 < 0 and index2 >= 0:
            return sum(map((lambda char: ord(char)), s2[:index2 + 1]))
        if index2 < 0 and index1 >= 0:
            return sum(map((lambda char: ord(char)), s1[:index1 + 1]))
        if index1 < 0 and index2 < 0:
            return 0

        if (index1, index2) in memo:
            return memo[index1, index2]

        if s1[index1] == s2[index2]:
            result = self.dp_top_down(s1, s2, index1 - 1, index2 - 1, memo)
        else:
            result = min(self.dp_top_down(s1, s2, index1, index2 - 1, memo) + ord(s2[index2]),
                         self.dp_top_down(s1, s2, index1 - 1, index2, memo) + ord(s1[index1]))
        memo[index1, index2] = result
        return result
