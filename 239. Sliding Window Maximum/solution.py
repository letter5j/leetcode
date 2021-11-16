from typing import List


class MonotonicQueue:
    queue: List[int] = list()

    def __init__(self):
        self.queue = list()

    def push(self, value: int):
        while len(self.queue) != 0 and self.queue[len(self.queue) - 1] < value:
            self.queue.pop(len(self.queue) - 1)
        self.queue.append(value)

    def get_max(self):
        return self.queue[0] if len(self.queue) != 0 else None

    def pop(self, value: int):
        if len(self.queue) != 0 and self.queue[0] == value:
            self.queue.pop(0)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result: List[int] = list()
        monotonic_queue = MonotonicQueue()
        for index in range(k - 1):
            monotonic_queue.push(nums[index])
        for index in range(k - 1, len(nums), 1):
            monotonic_queue.push(nums[index])
            result.append(monotonic_queue.get_max())
            monotonic_queue.pop(nums[index - k + 1])

        return result
