# 1136. Parallel Courses
# O(n) time, O(n) space


from typing import List
from collections import defaultdict


def parallel(n: int, relations: List[List[int]]) -> int:
    graph = defaultdict(set)
    degs = defaultdict(int)

    for prereq, course in relations:
        graph[prereq].add(course)
        degs[course] += 1

    # range(1, n) cuz not course 0
    queue = [course for course in range(1, n) if not degs[course]]

    res = 0
    study = 0

    while queue:
        next_queue = []
        for course in queue:
            study += 1
            for next_course in graph[course]:
                degs[next_course] -= 1
                if not degs[next_course]:
                    next_queue.append(next_course)
        queue = next_queue
        res += 1

    return res if study == n else -1


if __name__ == "__main__":
    # fmt: off
    print(parallel(3,[[1,3,],[2, 3]]))
    print(parallel(3, [[1,2],[2,3],[3,1]]))
    # fmt: on
