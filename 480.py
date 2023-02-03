# 480. Sliding Window Median
from typing import List
from heapq import heappush, heappop


def median_sliding_window(numbers: List[int], k: int) -> List[float]:
    def find_median():
        res = -max_heap[0] if k ^ 1 else min_heap[0] - max_heap[0]
        return float(res)

    max_heap, min_heap = [], []
    res = []
    to_del = set()

    for number in numbers[:k]:
        heappush(max_heap, -number)
        heappush(min_heap, -heappop(max_heap))
        if len(max_heap) < len(min_heap):
            heappush(max_heap, -heappop(min_heap))

    res.append(median := find_median())

    for i, number in enumerate(numbers[k:], k):
        prev = numbers[i - k]
        to_del.add(prev)

        balance = -1 if prev <= median else 1

        if number <= median:
            balance += 1
            heappush(max_heap, -number)
        else:
            balance -= 1
            heappush(min_heap, number)

        if balance < 0:
            heappush(max_heap, -heappop(min_heap))
        elif balance > 0:
            heappush(min_heap, -heappop(max_heap))

        while max_heap and -max_heap[0] in to_del:
            to_del.remove(-max_heap[0])
            heappop(max_heap)

        while min_heap and min_heap[0] in to_del:
            to_del.remove(min_heap[0])
            heappop(min_heap)

        res.append(median := find_median())

    return res


if __name__ == "__main__":
    numbers = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
    actual = median_sliding_window(numbers, k)
    print("Actual:   " + ", ".join(str(x) for x in actual))
    print("Expected: " + ", ".join(str(x) for x in expected))
