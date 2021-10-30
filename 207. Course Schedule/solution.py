from typing import Optional, Dict, Set, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list: List[List[int]] = self.build_adjacency_list(numCourses, prerequisites)
        visited = [False] * numCourses
        for course in range(numCourses):
            path_history = [False] * numCourses
            result = self.traverse(adjacency_list, course, visited, path_history)
            if not result:
                return False
        return True

    def traverse(self, adjacency_list: List[List[int]], course: int, visited: List[bool],
                 path_history: List[bool]) -> bool:
        if path_history[course]:
            return False
        if visited[course]:
            return True
        visited[course] = True
        path_history[course] = True
        next_course_list: List[int] = adjacency_list[course]
        for next_course in next_course_list:
            result = self.traverse(adjacency_list, next_course, visited, path_history)
            if not result:
                return result
        path_history[course] = False
        return True

    def build_adjacency_list(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:

        adjacency_list: List[List[int]] = list()
        for i in range(numCourses):
            adjacency_list.append(list())
        for prerequisite in prerequisites:
            course = prerequisite[0]
            pre_course = prerequisite[1]
            adjacency_list[pre_course].append(course)
        return adjacency_list
