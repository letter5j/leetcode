from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        return self.find_next_warmer_days(temperatures)

    def find_next_warmer_days(self, temperatures: List[int]) -> List[int]:
        result: List[int] = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = list()
        for i in range(len(temperatures) - 1, -1, -1):

            while len(stack) != 0 and stack[len(stack) - 1][1] <= temperatures[i]:
                stack.pop(len(stack) - 1)

            result[i] = (stack[len(stack) - 1][0] - i) if len(stack) != 0 else 0
            stack.append((i, temperatures[i]))
        return result
