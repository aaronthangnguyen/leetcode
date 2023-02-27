# 1631. path with minimum effort
from typing import List
from sys import maxsize
from heapq import heappush, heappop
from collections import deque


# SPFA
# O(r^2 * c^2) time, O(r * c) space
def path(heights: List[List[int]]) -> int:
    R, C = len(heights), len(heights[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    efforts = [[maxsize] * C for _ in range(R)]
    efforts[0][0] = 0

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            r, c = x + dx, y + dy

            if not (0 <= r < R and 0 <= c < C):
                continue

            next_effort = max(efforts[x][y], abs(heights[r][c] - heights[x][y]))
            if efforts[r][c] > next_effort:
                efforts[r][c] = next_effort
                queue.append((r, c))

    return efforts[-1][-1]


# Dijkstra
# O(r * c * log (r * c)) time, O(r * c) space
def path2(heights: List[List[int]]) -> int:
    R, C = len(heights), len(heights[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    efforts = [[maxsize] * C for _ in range(R)]
    efforts[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        effort, x, y = heappop(heap)
        if (x, y) == (R - 1, C - 1):
            return effort
        for dx, dy in dirs:
            r, c = x + dx, y + dy

            if not (0 <= r < R and 0 <= c < C):
                continue

            next_effort = max(effort, abs(heights[r][c] - heights[x][y]))
            if efforts[r][c] > next_effort:
                efforts[r][c] = next_effort
                heappush(heap, (next_effort, r, c))

    return -1


if __name__ == "__main__":
    print(path([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
    print(path2([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
