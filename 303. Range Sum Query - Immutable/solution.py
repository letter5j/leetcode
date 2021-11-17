from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list()
        count = 0
        for index in range(len(nums)):
            self.nums.append(nums[index] + count)
            count = count + nums[index]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - (self.nums[left - 1] if left > 0 else 0)
