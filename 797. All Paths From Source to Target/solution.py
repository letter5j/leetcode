from typing import Optional, Dict, Set, List


# Definition for singly-linked list.
class Node:
    def __init__(self, val: int, children: List[int]):
        self.val: int = val

        self.children: List[Node] = list()


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        return self.traverse(graph, 0)

    def traverse(self, graph: List[List[int]], index: int) -> List[List[int]]:

        all_path_to_end: List[List[int]] = list(list())

        if index == len(graph) - 1:
            return [[index]]
        for node in graph[index]:
            all_sub_path_to_end: List[List[int]] = self.traverse(graph, node)
            for sub_list in all_sub_path_to_end:
                sub_list.insert(0, index)
                all_path_to_end.append(sub_list)
        return all_path_to_end