# 502. IPO
# O(n log n) time, O(n) space

from typing import List
from heapq import heapify, heappush, heappop


def ipo(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    n = len(profits)

    cap_h = []
    pro_h = []

    for i in range(n):
        heappush(cap_h, (capital[i], profits[i]))

    for _ in range(k):
        while cap_h and cap_h[0][0] <= w:
            cap, pro = heappop(cap_h)
            heappush(pro_h, (-pro, cap))
        if pro_h:
            w -= heappop(pro_h)[0]

    return w


if __name__ == "__main__":
    print(ipo(2, 0, [1, 2, 3], [0, 1, 1]))
    print(ipo(3, 0, [1, 2, 3], [0, 1, 2]))
