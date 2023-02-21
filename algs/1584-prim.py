# O(e log v) time, O(v) space
from typing import List
from heapq import heapify, heappush, heappop


def prim(points: List[List[int]]) -> int:
    """
    1. Pick starting vertex
    2. Find edges that connect to new vertices, find minimum and add it tree
    3. Repeat until n - 1 edges
    """
    if not points:
        return 0

    n = len(points)
    heap = []
    x1, y1 = points[0]

    for p2 in range(1, n):
        x2, y2 = points[p2]
        d = abs(x1 - x2) + abs(y1 - y2)
        heap.append((d, 0, p2))
    heapify(heap)

    res = 0
    visited = set([0])
    count = n - 1

    while heap and count > 0:
        d, p1, p2 = heappop(heap)
        if p2 in visited:
            continue
        res += d
        visited.add(p2)

        for p3 in range(n):
            if p3 in visited:
                continue
            x2, y2 = points[p2]
            x3, y3 = points[p3]
            d2 = abs(x2 - x3) + abs(y2 - y3)
            heappush(heap, (d2, p2, p3))

        count -= 1

    return res


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(prim(points))
