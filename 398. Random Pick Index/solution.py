import secrets
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        random_index = -1
        for index, num in enumerate(self.nums):

            if num == target:
                count = count + 1
                random_value = secrets.randbelow(count)

                if random_value == 0:
                    random_index = index

        return random_index
