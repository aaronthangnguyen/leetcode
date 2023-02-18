# 1584 - Min Cost to Connect All Points (Prim's)
# O(elog v) time, O(v) space

from typing import List
from heapq import heapify, heappush, heappop


class Edge:
    def __init__(self, point1: int, point2: int, cost: int):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other: "Edge"):
        return self.cost < other.cost


def min_cost_to_connect_all_points(points: List[List[int]]) -> int:
    if not points:
        return 0

    size = len(points)
    pq = []
    visited = set()
    res = 0
    count = size - 1

    x1, y1 = points[0]
    for i in range(1, size):
        x2, y2 = points[i]
        cost = abs(x1 - x2) + abs(y1 - y2)
        edge = Edge(0, i, cost)
        pq.append(edge)

    heapify(pq)

    visited.add(0)
    while pq and count > 0:
        edge = heappop(pq)
        point1 = edge.point1
        point2 = edge.point2
        cost = edge.cost
        if point2 not in visited:
            res += cost
            visited.add(point2)
            for i in range(size):
                if i not in visited:
                    new_x1, new_y1 = points[point2]
                    new_x2, new_y2 = points[i]
                    new_cost = abs(new_x1 - new_x2) + abs(new_y1 - new_y2)
                    heappush(pq, Edge(point2, i, new_cost))
            count -= 1
    return res


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(min_cost_to_connect_all_points(points))
