from typing import Optional, Dict, Set, List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group: Dict[int, bool] = dict()
        adjacency_list: List[List[int]] = self.build_adjacency_list(n, dislikes)
        visited: List[bool] = [False] * n
        for node in range(n):
            group.setdefault(node, False)
            result = self.traverse(adjacency_list, group, node, group.get(node), visited)
            if not result:
                return False
        return True

    def traverse(self, graph: List[List[int]], group: Dict[int, bool], node: int, group_category: bool,
                 visited: List[bool]) -> bool:

        if node in group and group[node] != group_category:
            return False
        if visited[node]:
            return True
        group[node] = group_category
        visited[node] = True
        for connect_node in graph[node]:
            result = self.traverse(graph, group, connect_node, not group_category, visited)
            if not result:
                return False

        return True

    def build_adjacency_list(self, n: int, dislikes: List[List[int]]):
        adjacency_list: List[List[int]] = list()
        for i in range(n):
            adjacency_list.append(list())
        for dislike_pair in dislikes:
            source = dislike_pair[0] - 1
            target = dislike_pair[1] - 1
            adjacency_list[source].append(target)
            adjacency_list[target].append(source)
        return adjacency_list

