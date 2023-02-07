# 207. Course Schedule
# O(v^2 + e) time, O(v + e) space

from typing import List


def course_schedule(courses: int, prereqs: List[List[int]]) -> bool:
    def dfs(course: int) -> bool:
        if course in visited:
            return False
        if not graph[course]:
            return True

        visited.add(course)
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        visited.remove(course)
        graph[course] = []  # path compression
        return True

    graph = [[] for _ in range(courses)]
    for course, prereq in prereqs:
        graph[course].append(prereq)
    visited = set()

    for course in range(courses):
        if not dfs(course):
            return False

    return True
