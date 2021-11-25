import bisect
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        return self.dp_binary_search(nums)

    def dp_solution(self, nums: List[int]) -> int:

        nums_length = len(nums)
        dp: List[int] = [1] * nums_length

        for i in range(nums_length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def dp_binary_search(self, nums: List[int]):
        dp: List[int] = list()
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)
