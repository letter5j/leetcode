from typing import List, Dict, Tuple


class Solution:
    def canPartition_bottom_up(self, nums: List[int]) -> bool:
        # a = b
        # sum = a + b
        # sum = 2a
        # sum / 2 = a
        nums_length = len(nums)
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        nums_sum = int(nums_sum / 2)
        dp: List[List[bool]] = [[False] * (nums_sum + 1) for _ in range(nums_length + 1)]

        for i in range(1, nums_length + 1):
            dp[i][0] = True
        for i in range(1, nums_sum + 1):
            dp[0][i] = False

        for i in range(1, nums_length + 1):
            for j in range(1, nums_sum + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]

        return dp[nums_length][nums_sum]

    def canPartition_top_down(self, nums: List[int]) -> bool:
        # a = b
        # sum = a + b
        # sum = 2a
        # sum / 2 = a
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        nums_sum = int(nums_sum / 2)
        memo: Dict[Tuple[int, int], bool] = dict()
        return self.dp_top_down(nums, len(nums) - 1, nums_sum, memo)

    def dp_top_down(self, nums: List[int], index: int, sum_value: int, memo: Dict[Tuple[int, int], bool]) -> bool:

        if sum_value == 0:
            return True
        if index < 0:
            return False

        if (index, sum_value) in memo:
            return memo[index, sum_value]

        if sum_value - nums[index - 1] < 0:
            result = self.dp_top_down(nums, index - 1, sum_value, memo)
        else:
            result = self.dp_top_down(nums, index - 1, sum_value - nums[index - 1], memo) or \
                     self.dp_top_down(nums, index - 1, sum_value, memo)

        memo[index, sum_value] = result
        return result
