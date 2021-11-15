from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.find_next_greater_element(nums)

    def find_next_greater_element(self, nums: List[int]) -> List[int]:
        numbers_duble: List[int] = nums * 2
        result: List[int] = [-1] * len(numbers_duble)
        stack: List[int] = list()
        for i in range(len(numbers_duble) - 1, -1, -1):

            while len(stack) != 0 and stack[len(stack) - 1] <= numbers_duble[i]:
                stack.pop(len(stack) - 1)

            result[i] = stack[len(stack) - 1] if len(stack) != 0 else -1
            stack.append(numbers_duble[i])
        return result[: len(nums)]
