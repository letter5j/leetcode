from typing import List, Dict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_num = 0
        result = 0
        k_map: Dict[int, int] = dict()
        k_map[0] = 1
        for index, num in enumerate(nums):
            sum_num = sum_num + num

            difference = sum_num - k

            if difference in k_map:
                result = result + k_map[difference]

            k_map[sum_num] = 1 + (k_map[sum_num] if sum_num in k_map else 0)
        return result
