from typing import List


class UnionFindInterface:
    def __init__(self, n: int):
        self.count: int = 0
        self.parent: List[int] = list()
        self.size: List[int] = list()
        pass

    def union(self, p: int, q: int):
        pass

    def find(self, p: int) -> int:
        pass

    def connected(self, p: int, q: int) -> bool:
        pass

    def count(self):
        return self.count


class UnionFind(UnionFindInterface):

    def __init__(self, n: int):
        super().__init__(n)
        self.count = n
        for i in range(n):
            self.parent.append(i)
            self.size.append(1)

    def union(self, p: int, q: int):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return

        if self.size[parent_p] > self.size[parent_q]:
            self.parent[parent_q] = parent_p
            self.size[parent_p] = self.size[parent_p] + self.size[parent_q]
        else:
            self.parent[parent_p] = parent_q
            self.size[parent_q] = self.size[parent_q] + self.size[parent_p]
        self.count = self.count - 1

    def find(self, p: int) -> int:
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)
