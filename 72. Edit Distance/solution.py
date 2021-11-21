from typing import Dict, Tuple, List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp(word1, word2, len(word1) - 1, len(word2) - 1, memo)

    def dp(self, word1: str, word2: str, word1_index: int, word2_index: int, memo: Dict[Tuple[int, int], int]) -> int:

        if word1_index < 0:
            return word2_index + 1  # insert n words
        if word2_index < 0:
            return word1_index + 1  # delete n words

        if (word1_index, word2_index) in memo:
            return memo[(word1_index, word2_index)]

        if word1[word1_index] == word2[word2_index]:
            result = self.dp(word1, word2, word1_index - 1, word2_index - 1, memo)  # move left without change
        else:
            result = min(
                self.dp(word1, word2, word1_index, word2_index - 1, memo) + 1,  # insert
                self.dp(word1, word2, word1_index - 1, word2_index, memo) + 1,  # delete
                self.dp(word1, word2, word1_index - 1, word2_index - 1, memo) + 1  # replace
            )
        memo[(word1_index, word2_index)] = result

        return result

    def min_distance_bottom_up(self, word1: str, word2: str) -> int:

        dp: List[List[int]] = list()

        word1_length = len(word1)
        word2_length = len(word2)

        for i in range(0, word1_length + 1, 1):
            j = [i] * (word2_length + 1)
            dp.append(j)
        for j in range(0, word2_length + 1, 1):
            dp[0][j] = j
        for i in range(1, word1_length + 1, 1):

            for j in range(1, word2_length + 1, 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # move left without change
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,  # insert
                        dp[i - 1][j] + 1,  # delete
                        dp[i - 1][j - 1] + 1  # replace
                    )

        return dp[word1_length][word2_length]
