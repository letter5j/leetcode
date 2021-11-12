from queue import PriorityQueue


class LargerNode:
    def __init__(self, value: int):
        self.value = value

    def __gt__(self, other):
        return self.value < other.value


class SmallerNode:
    def __init__(self, value: int):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value


class MedianFinder:

    def __init__(self):
        self.larger_queue = PriorityQueue()
        self.smaller_queue = PriorityQueue()
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count = self.count + 1
        if self.smaller_queue.qsize() == 0 or num <= self.smaller_queue.queue[0].value:
            self.smaller_queue.put(LargerNode(num))
            if self.smaller_queue.qsize() - self.larger_queue.qsize() > 1:
                self.larger_queue.put(SmallerNode(self.smaller_queue.get().value))
        else:
            self.larger_queue.put(SmallerNode(num))
            if abs(self.smaller_queue.qsize() - self.larger_queue.qsize()) == 1:
                self.smaller_queue.put(LargerNode(self.larger_queue.get().value))

    def findMedian(self) -> float:

        if self.count % 2 == 0:
            return (self.smaller_queue.queue[0].value + self.larger_queue.queue[0].value) / 2
        else:
            return self.smaller_queue.queue[0].value
