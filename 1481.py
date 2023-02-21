# 1481. Least Number of Unique Integers after K Removals
# O(n + k log n) time, O(n) space

from typing import List
from collections import Counter
from heapq import heapify, heappop


def find(numbers: List[int], k: int) -> int:
    heap = list(Counter(numbers).values())
    heapify(heap)
    while k > 0:
        k -= heappop(heap)
    return len(heap) + (k < 0)


if __name__ == "__main__":
    print(find([4, 3, 1, 1, 3, 3, 2], 3))
