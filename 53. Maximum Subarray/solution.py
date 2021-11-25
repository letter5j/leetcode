from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp_prev = nums[0]
        max_sum = nums[0]
        for index in range(1, len(nums), 1):
            dp_prev = max(dp_prev + nums[index], nums[index])
            max_sum = dp_prev if dp_prev > max_sum else max_sum
        return max_sum
