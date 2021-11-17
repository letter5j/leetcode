from collections import deque
from typing import Deque


class MyQueue:

    def __init__(self):
        self.queue: Deque[int] = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
