from __future__ import annotations

from typing import Dict, List


class Node:
    key: int
    value: int
    count: int
    prev: Node = None
    next: Node = None

    def __init__(self, key: int, value: int, count: int):
        self.key = key
        self.value = value
        self.count = count


class BiDirectionalLinkedList:
    size: int

    # for first / last node change
    head: Node
    tail: Node

    def __init__(self):
        self.head: Node = Node(0, 0, 0)
        self.tail: Node = Node(0, 0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_last(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        self.size = self.size + 1

    def remove_first(self):
        if self.size == 0:
            return
        next_node = self.head.next
        next_node.next.prev = self.head
        self.head.next = next_node.next
        self.size = self.size - 1

    def remove(self, node: Node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size = self.size - 1

    def __len__(self) -> int:
        return self.size


class LFUCache:
    capacity: int
    cache: Dict[int, Node]
    node_list_stack: Dict[int, BiDirectionalLinkedList]
    min_count: int

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.node_list_stack = dict()
        self.min_count = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            original_count = node.count
            self.node_list_stack[original_count].remove(node)
            if self.node_list_stack[original_count].size == 0:
                self.node_list_stack.pop(original_count, None)
                if self.min_count == original_count:
                    self.min_count = self.min_count + 1
            node.count = node.count + 1
            if node.count not in self.node_list_stack:
                self.node_list_stack[node.count] = BiDirectionalLinkedList()
            self.node_list_stack[node.count].add_last(node)
            return self.cache.get(key).value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            original_count = node.count
            self.node_list_stack[original_count].remove(node)
            if self.node_list_stack[original_count].size == 0:
                self.node_list_stack.pop(original_count, None)
                if self.min_count == original_count:
                    self.min_count = self.min_count + 1
            node.count = node.count + 1
            node.value = value
            if node.count not in self.node_list_stack:
                self.node_list_stack[node.count] = BiDirectionalLinkedList()
            self.node_list_stack[node.count].add_last(node)
        else:
            if len(self.cache) == self.capacity:
                if self.capacity == 0:
                    return
                self.cache.pop(self.node_list_stack[self.min_count].head.next.key, None)
                self.node_list_stack[self.min_count].remove_first()
                if self.node_list_stack[self.min_count].size == 0:
                    self.node_list_stack.pop(self.min_count, None)
            new_node: Node = Node(key, value, 0)
            if 0 not in self.node_list_stack:
                self.node_list_stack[0] = BiDirectionalLinkedList()
            self.node_list_stack[0].add_last(new_node)
            self.cache[key] = new_node
            self.min_count = 0


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

