from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = 0
        longest_sub_string_length = 0
        char_in_window: Dict[str, int] = dict()
        for index in range(len(s)):
            if s[index] in char_in_window and char_in_window[s[index]] >= start_index:
                start_index = char_in_window[s[index]] + 1
            char_in_window[s[index]] = index
            longest_sub_string_length = max(longest_sub_string_length, index - start_index + 1)
        return longest_sub_string_length
