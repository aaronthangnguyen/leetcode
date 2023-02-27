# 787. Cheapest Flights Within K Stops
# O(v * e) time, O(v) space

from typing import List
from sys import maxsize


def find(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    if src == dst:
        return 0

    prevs = [maxsize] * n
    currs = [maxsize] * n

    prevs[src] = 0
    currs[src] = 0

    for _ in range(k + 1):
        for prev, curr, cost in flights:
            if prevs[prev] < float("inf"):
                currs[curr] = min(currs[curr], prevs[prev] + cost)
        prevs = currs.copy()

    return currs[dst] if currs[dst] != maxsize else -1


if __name__ == "__main__":
    print(
        find(
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
        )
    )
