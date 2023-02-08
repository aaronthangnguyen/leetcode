# 436. Find Right Interval
# O(nlogn n) time, O(n) space

from typing import List
from heapq import heapify, heappush, heappop


def find_right_interval(intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    res = [-1] * n
    start_heap, end_heap = [], []

    for i in range(n):
        heappush(start_heap, (intervals[i][0], i))

    while start_heap:
        start, i = heappop(start_heap)
        while end_heap and start >= end_heap[0][0]:
            res[heappop(end_heap)[1]] = i
        if start == intervals[i][1]:
            res[i] = i
        else:
            heappush(end_heap, (intervals[i][1], i))

    return res


if __name__ == "__main__":
    print(find_right_interval([[3, 4], [2, 3], [1, 2]]))
    print(find_right_interval([[1, 4], [2, 3], [3, 4]]))
