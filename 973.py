# 973. K Closest Points to Origin
# O(nlog k) time, O(k) space

from typing import List
from heapq import heapify, heappush, heappushpop


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for x, y in points:
        d = x**2 + y**2
        if len(heap) < k:
            heappush(heap, [-d, x, y])
        else:
            heappushpop(heap, [-d, x, y])
    return [[x, y] for d, x, y in heap]


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    print(k_closest(points, 2))
