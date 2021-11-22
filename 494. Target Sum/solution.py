from typing import List, Dict, Tuple


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo: Dict[Tuple[int, int], int] = dict()
        return self.dp(nums, target, 0, memo)

    def dp(self, nums: List[int], target: int, index: int, memo: Dict[Tuple[int, int], int]):

        if index == len(nums) and target == 0:
            return 1
        if index >= len(nums):
            return 0

        if (target, index) in memo:
            return memo[(target, index)]

        result = self.dp(nums, target + nums[index], index + 1, memo) + \
                 self.dp(nums, target - nums[index], index + 1, memo)

        memo[(target, index)] = result
        return result
