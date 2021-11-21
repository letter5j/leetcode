from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        return self.dp_solution(nums)

    def dp_solution(self, nums: List[int]) -> int:

        nums_length = len(nums)
        dp: List[int] = [1] * nums_length

        for i in range(nums_length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
