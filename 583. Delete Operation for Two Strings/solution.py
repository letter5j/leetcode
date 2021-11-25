from typing import Dict, Tuple, List


class Solution:
    def minDistance_bottom_up(self, word1: str, word2: str) -> int:

        word1_length = len(word1)
        word2_length = len(word2)

        dp: List[List[int]] = [[0] * (word2_length + 1) for _ in range(word1_length + 1)]

        for row in range(word1_length + 1):
            dp[row][0] = row
        for column in range(word2_length + 1):
            dp[0][column] = column

        for row in range(1, word1_length + 1):
            for column in range(1, word2_length + 1):
                if word1[row - 1] == word2[column - 1]:
                    dp[row][column] = dp[row - 1][column - 1]
                else:
                    dp[row][column] = min(
                        dp[row - 1][column] + 1,
                        dp[row][column - 1] + 1
                    )

        return dp[word1_length][word2_length]

    def minDistance_top_down(self, word1: str, word2: str) -> int:
        memo: Dict[Tuple[int, int], int] = dict()

        result = self.dp_top_down(word1, word2, len(word1) - 1, len(word2) - 1, memo)
        return result

    def dp_top_down(self, word1: str, word2: str, index1: int, index2: int, memo: Dict[Tuple[int, int], int]) -> int:

        if index1 < 0 and index2 >= 0:
            return index2 + 1
        if index2 < 0 and index1 >= 0:
            return index1 + 1
        if index1 < 0 and index2 < 0:
            return 0

        if (index1, index2) in memo:
            return memo[index1, index2]

        if word1[index1] == word2[index2]:
            result = self.dp_top_down(word1, word2, index1 - 1, index2 - 1, memo)
        else:
            result = min(self.dp_top_down(word1, word2, index1, index2 - 1, memo) + 1,
                         self.dp_top_down(word1, word2, index1 - 1, index2, memo) + 1)
        memo[index1, index2] = result
        return result
