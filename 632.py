# 632. Smallest Range Covering Elements from K Lists
# O(n log k) time, O(k) space; n: |elements|, k: |arrays|

from typing import List
from heapq import heapify, heappush, heappop
from sys import maxsize


def smallest(arrays: List[List[int]]) -> List[int]:
    n = len(arrays)
    heap = []

    max_val = 0
    for i, array in enumerate(arrays):
        heap.append((array[0], i, 0))
        # (value, index of array, index of element)
        max_val = max(max_val, array[0])
    heapify(heap)

    res = [heap[0][0], max_val]

    while True:
        _, row, col = heappop(heap)
        array = arrays[row]

        if col == len(array) - 1:
            break

        next = array[col + 1]

        max_val = max(max_val, next)

        heappush(heap, (next, row, col + 1))

        if max_val - heap[0][0] < res[1] - res[0]:
            res = [heap[0][0], max_val]

    return res


if __name__ == "__main__":
    numbers = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(smallest(numbers))
