from typing import Dict, List, Tuple


class Solution:
    def longestCommonSubsequence_top_down(self, text1: str, text2: str) -> int:

        new_text1, new_text2 = self.remove_unnecessary_char(text1, text2)
        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp_top_down(new_text1, new_text2, len(new_text1) - 1, len(new_text2) - 1, memo)

    def dp_top_down(self, text1: str, text2: str, index1: int, index2: int, memo: Dict[Tuple[int, int], int]) -> int:

        if index1 < 0 or index2 < 0:
            return 0

        if (index1, index2) in memo:
            return memo[index1, index2]

        if text1[index1] == text2[index2]:
            result = self.dp_top_down(text1, text2, index1 - 1, index2 - 1, memo) + 1
        else:
            result = max(
                self.dp_top_down(text1, text2, index1 - 1, index2, memo),
                self.dp_top_down(text1, text2, index1, index2 - 1, memo)
            )
        memo[index1, index2] = result
        return result

    def longestCommonSubsequence_bottom_up(self, text1: str, text2: str) -> int:

        new_text1, new_text2 = self.remove_unnecessary_char(text1, text2)

        text1_length = len(new_text1)
        text2_length = len(new_text2)
        dp: List[List[int]] = [[0] * (text2_length + 1) for i in range(text1_length + 1)]

        for row in range(1, text1_length + 1):
            for column in range(1, text2_length + 1):

                if new_text1[row - 1] == new_text2[column - 1]:
                    dp[row][column] = dp[row - 1][column - 1] + 1
                else:
                    dp[row][column] = max(dp[row - 1][column], dp[row][column - 1])
        return dp[text1_length][text2_length]

    def remove_unnecessary_char(self, text1: str, text2: str) -> Tuple[str, str]:
        text1_map: Dict[str, bool] = dict()
        text2_map: Dict[str, bool] = dict()
        for char in text1:
            text1_map[char] = True
        new_text2 = ""
        for char in text2:
            if char not in text1_map:
                continue
            text2_map[char] = True
            new_text2 = new_text2 + char
        new_text1 = ""
        for char in text1:
            if char not in text2_map:
                continue
            new_text1 = new_text1 + char
        return new_text1, new_text2
