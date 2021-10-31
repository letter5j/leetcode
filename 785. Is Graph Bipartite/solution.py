from typing import Optional, Dict, Set, List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group: Dict[int, bool] = dict()
        # adjacency_matrix: List[List[int]] = self.build_adjacency_matrix(graph)
        visited: List[bool] = [False] * len(graph)
        for node in range(len(graph)):
            group.setdefault(node, False)
            result = self.traverse(graph, group, node, group.get(node), visited)
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
