from typing import Dict, List, Tuple


class Solution:
    def maxCoins_top_down(self, nums: List[int]) -> int:
        memo: Dict[Tuple[int, int], int] = dict()
        nums = [1] + nums + [1]
        nums_len = len(nums)
        return self.dp_top_down(nums, 0, nums_len - 1, memo)

    def dp_top_down(self, nums: List[int], start_index: int, end_index: int, memo: Dict[Tuple[int, int], int]) -> int:
        if start_index == end_index:
            return 0
        if (start_index, end_index) in memo:
            return memo[start_index, end_index]

        result = 0
        for i in range(start_index + 1, end_index):
            coin_sum = nums[start_index] * nums[i] * nums[end_index]

            result = max(result,
                         self.dp_top_down(nums, start_index, i, memo) +
                         self.dp_top_down(nums, i, end_index,memo) +
                         coin_sum)
        memo[start_index, end_index] = result
        return result
