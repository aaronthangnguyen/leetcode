# 743. Network Delay Time
# O(v + e log v) time, O(v + e) space

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


def network(times: List[List[int]], n: int, k: int):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    visited = set()
    heap = [(0, k)]
    res = 0

    while heap:
        cost, node = heappop(heap)
        if node in visited:
            continue

        visited.add(node)
        res = max(res, cost)

        for next_node, next_weight in graph[node]:
            if next_node in visited:
                continue

            next_cost = cost + next_weight
            heappush(heap, (next_cost, next_node))

    return res if len(visited) == n else -1


if __name__ == "__main__":
    print(network([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
