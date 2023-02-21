# O(e log e) time, O(v) space
from typing import List
from heapq import heapify, heappop


def kruskal(points: List[List[int]]) -> int:
    """
    1. Generate edges ascendingly sorted by weight
    2. Add edges into MST. Skip edges that would produce cycles
    3. Repeat until n - 1 edges
    """
    if not points:
        return 0

    n = len(points)
    heap = []

    for p1 in range(n):
        x1, y1 = points[p1]
        for p2 in range(p1 + 1, n):
            x2, y2 = points[p2]
            d = abs(x1 - x2) + abs(y1 - y2)
            heap.append((d, p1, p2))
    heapify(heap)

    res = 0
    count = n - 1
    uf = UnionFind(n)

    while heap and count > 0:
        d, p1, p2 = heappop(heap)
        if not uf.connected(p1, p2):
            uf.union(p1, p2)
            res += d
            count -= 1

    return res


class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(kruskal(points))
