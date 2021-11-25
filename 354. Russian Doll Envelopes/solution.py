import bisect
from functools import cmp_to_key
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def compare(item1: List[int], item2: List[int]):
            if item1[0] > item2[0]:
                return 1
            elif item1[0] == item2[0]:
                return item2[1] - item1[1]
            else:
                return -1

        sorted_envelopes = sorted(envelopes, key=cmp_to_key(compare))

        return self.dp_binary_search(sorted_envelopes)

    def dp_binary_search(self, envelopes: List[List[int]]):
        dp: List[int] = list()
        for envelope in envelopes:
            index = bisect.bisect_left(dp, envelope[1])
            if index == len(dp):
                dp.append(envelope[1])
            else:
                dp[index] = envelope[1]
        return len(dp)

    def dp(self, envelopes: List[List[int]]) -> int:
        envelopes_length = len(envelopes)
        dp: List[int] = [1] * envelopes_length
        max_count = 1
        for i in range(1, envelopes_length, 1):
            x = envelopes[i][0]
            y = envelopes[i][1]
            for j in range(i):
                if x > envelopes[j][0] and y > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_count:
                        max_count = dp[i]
        return max_count
