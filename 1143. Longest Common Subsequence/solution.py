from typing import Dict, List, Tuple


class Solution:
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
