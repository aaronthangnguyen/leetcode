# 210. Course Schedule II
# O(v + e) time, O(v + e) space

from typing import List
from collections import defaultdict, deque


def schedule(courses: int, prereqs: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    indeg = defaultdict(int)

    # populate
    for course, prereq in prereqs:
        graph[prereq].append(course)
        indeg[course] += 1

    # queue for 0 in-degree
    queue = deque([course for course in range(courses) if course not in indeg])

    # topological sorted order
    res = []

    while queue:
        prereq = queue.popleft()
        res.append(prereq)

        for course in graph[prereq]:
            indeg[course] -= 1

            if indeg[course] == 0:
                queue.append(course)

    return res if len(res) == courses else []


if __name__ == "__main__":
    print(schedule(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
