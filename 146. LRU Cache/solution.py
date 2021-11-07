from __future__ import annotations

from typing import Dict, List


class Node:
    key: int
    value: int
    prev: Node = None
    next: Node = None

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value


class BiDirectionalLinkedList:
    size: int

    # for first / last node change
    head: Node
    tail: Node

    def __init__(self):
        self.head: Node = Node(0, 0)
        self.tail: Node = Node(0, 0)
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


class LRUCache:
    capacity: int
    cache: Dict[int, Node]
    node_list: BiDirectionalLinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.node_list = BiDirectionalLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self.node_list.remove(node)
            self.node_list.add_last(node)
            return self.cache.get(key).value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            self.node_list.remove(node)
            node.value = value
            self.node_list.add_last(node)
        else:
            if len(self.node_list) == self.capacity:
                self.cache.pop(self.node_list.head.next.key, None)
                self.node_list.remove_first()
            new_node: Node = Node(key, value)
            self.node_list.add_last(new_node)
            self.cache[key] = new_node
