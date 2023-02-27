# 2093. Minimum Cost to Reach City With Discounts
# O(e log e) time, O(e) space

from typing import List
from collections import defaultdict
from heapq import heapify, heappush, heappop


def minimum(n: int, highways: List[List[int]], discounts: int) -> int:
    graph = defaultdict(list)
    heap = [(0, 0, discounts)]
    visited = {}

    for city1, city2, toll in highways:
        graph[city1].append((city2, toll))
        graph[city2].append((city1, toll))

    while heap:
        cost, city, disc = heappop(heap)

        if city == n - 1:
            return cost

        # skip cuz city visited before and didn't cost extra discount
        if city in visited and visited[city] >= disc:
            continue
        visited[city] = disc

        for next_city, next_toll in graph[city]:
            heappush(heap, (cost + next_toll, next_city, disc))
            if disc > 0:
                heappush(heap, (cost + next_toll // 2, next_city, disc - 1))

    return -1


if __name__ == "__main__":
    highways = [[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]]
    print(minimum(5, highways, 1))
