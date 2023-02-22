# 358. Rearrange String k Distance Apart
# O(n) time, O(1) space

from collections import Counter
from heapq import heapify, heappush, heappop


def rearrange(stg: str, k: int) -> str:
    if k < 2:
        return stg

    res = []
    cooldown = {}
    heap = [(-f, c) for c, f in Counter(stg).items()]
    heapify(heap)

    while heap:
        f, c = heappop(heap)
        res.append(c)
        f += 1
        if f < 0:
            cooldown[c] = [f, c]
        if len(res) >= k and res[-k] in cooldown:
            pf, pc = cooldown.pop(res[-k])
            heappush(heap, (pf, pc))

    return "".join(res) if len(res) == len(stg) else ""


if __name__ == "__main__":
    print(rearrange("aabbcc", 3))
