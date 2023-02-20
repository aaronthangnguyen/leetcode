# 703. Kth Largest Element in a Stream
# O(klog n) time, O(k) space


from typing import List
from heapq import heapify, heappush, heappop, heappushpop, nlargest


class KLargest:
    def __init__(self, k: int, numbers: List[int]):
        self.k = k
        self.heap = nlargest(k, numbers)
        heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappushpop(self.heap, val)
        return self.heap[0]


if __name__ == "__main__":
    obj = KLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
