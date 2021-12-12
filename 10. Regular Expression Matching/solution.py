from typing import Dict, List, Tuple


class Solution:
    def __init__(self):
        self.DOT = "."
        self.ASTERISK = "*"

    def isMatch_top_down(self, s: str, p: str) -> bool:
        memo: Dict[Tuple[int, int], bool] = dict()
        result = self.dp_top_down(s, p, 0, 0, memo)
        return result

    def dp_top_down(self, s: str, p: str, s_index: int, p_index: int, memo: Dict[Tuple[int, int], bool]) -> bool:

        if s_index == len(s) and p_index == len(p):
            return True

        if p_index == len(p):
            return False

        if (s_index, p_index) in memo:
            return memo[s_index, p_index]

        if (s_index < len(s)) and (s[s_index] == p[p_index] or self.DOT == p[p_index]):
            if (p_index != len(p) - 1) and self.ASTERISK == p[p_index + 1]:
                result = self.dp_top_down(s, p, s_index + 1, p_index, memo) \
                         or self.dp_top_down(s, p, s_index + 1, p_index + 2, memo) \
                         or self.dp_top_down(s, p, s_index, p_index + 2, memo)
            else:
                result = self.dp_top_down(s, p, s_index + 1, p_index + 1, memo)
        else:
            if (p_index != len(p) - 1) and self.ASTERISK == p[p_index + 1]:
                result = self.dp_top_down(s, p, s_index, p_index + 2, memo)
            else:
                result = False
        memo[s_index, p_index] = result
        return result
