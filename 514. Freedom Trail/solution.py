from typing import List, Dict, Tuple


class Solution:

    def findRotateSteps_top_down(self, ring: str, key: str) -> int:

        memo: Dict[Tuple[int, int], int] = dict()
        char_indexes_memo: Dict[str, List[int]] = dict()

        result = self.dp_top_down(ring, key, 0, 0, memo, char_indexes_memo)

        return result

    def dp_top_down(self, ring: str, key: str, ring_index: int, key_index: int, memo: Dict[Tuple[int, int], int],
                    char_indexes_memo: Dict[str, List[int]]) -> int:

        if key_index == len(key):
            return 0

        if (ring_index, key_index) in memo:
            return memo[ring_index, key_index]

        target_char = key[key_index]

        char_indexes = self.find_char_indexes_in_string(ring, target_char, char_indexes_memo)

        ring_length = len(ring)

        for index in char_indexes:

            # clockwise
            clockwise = index - ring_index if index >= ring_index else index - ring_index + ring_length
            # anticlockwise
            anticlockwise = ring_index - index if ring_index >= index else ring_index - index + ring_length

            result = self.dp_top_down(ring, key, index, key_index + 1, memo, char_indexes_memo) + min(clockwise,
                                                                                                      anticlockwise) + 1
            if (ring_index, key_index) in memo:
                if result < memo[ring_index, key_index]:
                    memo[ring_index, key_index] = result
            else:
                memo[ring_index, key_index] = result

        return memo[ring_index, key_index]

    def find_char_indexes_in_string(self, string: str, target_char: str, memo: Dict[str, List[int]]) -> List[int]:
        if target_char in memo:
            return memo[target_char]
        result = list()
        for i, character in enumerate(string):
            if target_char == character:
                result.append(i)
        memo[target_char] = result
        return result
