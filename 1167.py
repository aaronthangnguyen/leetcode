# 1167. Minimum Cost to Connect Sticks
# O(nlog n) time, O(n) space

from typing import List
from heapq import heapify, heappush, heappop


def connect_sticks(sticks: List[int]) -> int:
    heapify(sticks)

    res = 0
    while len(sticks) > 1:
        x, y = heappop(sticks), heappop(sticks)
        heappush(sticks, x + y)
        res += x + y

    return res


if __name__ == "__main__":
    print(connect_sticks([2, 4, 3]))
