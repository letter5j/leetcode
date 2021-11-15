from typing import List, Dict


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        next_element: Dict[int, int] = self.find_next_greater_element(nums2)

        result: List[int] = list()
        for num in nums1:
            result.append(next_element[num])
        return result

    def find_next_greater_element(self, nums: List[int]) -> Dict[int, int]:

        result: Dict[int, int] = dict()
        stack: List[int] = list()
        for i in range(len(nums) - 1, -1, -1):

            while len(stack) != 0 and stack[len(stack) - 1] < nums[i]:
                stack.pop(len(stack) - 1)

            result[nums[i]] = stack[len(stack) - 1] if len(stack) != 0 else -1
            stack.append(nums[i])
        return result
