from typing import Dict, Tuple


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
