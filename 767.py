# 767. Reorganize String
# O(n) time, O(1) space; size is 26

from heapq import heapify, heappush, heappop
from collections import Counter


def reorganize(stg: str) -> str:
    res = []
    heap = [(-v, k) for k, v in Counter(stg).items()]
    heapify(heap)
    prev_v, prev_k = 0, ""

    while heap:
        v, k = heappop(heap)
        res.append(k)
        if prev_v < 0:
            heappush(heap, (prev_v, prev_k))
        prev_v, prev_k = v + 1, k

    return "".join(res) if len(res) == len(stg) else ""


if __name__ == "__main__":
    print(reorganize("aab"))
    print(reorganize("aaab"))
