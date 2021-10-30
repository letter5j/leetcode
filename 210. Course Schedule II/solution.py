from typing import Optional, Dict, Set, List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list: List[List[int]] = self.build_adjacency_list(numCourses, prerequisites)
        visited = [False] * numCourses
        weight_list: List[int] = [1] * numCourses
        for course in range(numCourses):
            path_history = [False] * numCourses
            result = self.traverse(adjacency_list, course, visited, path_history, weight_list)
            if not result:
                return []
        return sorted(range(len(weight_list)), key=lambda course: weight_list[course], reverse=True)

    def traverse(self, adjacency_list: List[List[int]], course: int, visited: List[bool],
                 path_history: List[bool], weight_list: List[int]) -> bool:
        if path_history[course]:
            return False
        if visited[course]:
            return True
        visited[course] = True
        path_history[course] = True
        weight = 1
        next_course_list: List[int] = adjacency_list[course]
        for next_course in next_course_list:
            result = self.traverse(adjacency_list, next_course, visited, path_history, weight_list)
            if not result:
                return result
            weight = weight + weight_list[next_course]
        weight_list[course] = weight
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
