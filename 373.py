# 373. Find K Pairs with Smallest Sums
# O(k log k) time, O(k) space


from typing import List
from heapq import heapify, heappush, heappop


def k_smallest_pairs(A: List[int], B: List[int], k: int) -> List[List[int]]:
    m, n = len(A), len(B)

    heap = []

    for i in range(min(m, k)):
        el = (A[i] + B[0], i, 0)
        heap.append(el)
    heapify(heap)

    res = []

    while heap and len(res) < k:
        _, i, j = heappop(heap)
        res.append([A[i], B[j]])
        if j + 1 < n:
            el = (A[i] + B[j + 1], i, j + 1)
            heappush(heap, el)

    return res
