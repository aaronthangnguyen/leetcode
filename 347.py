# 347. Top K Frequent Elements
# O(nlog k) time, O(n) space

from typing import List
from collections import Counter
from heapq import nlargest


def top_k(numbers: List[int], k: int) -> List[int]:
    freqs = [(v, k) for k, v in Counter(numbers).items()]
    return [k for _, k in nlargest(k, freqs)]


if __name__ == "__main__":
    print(top_k([1, 1, 1, 2, 2, 3], 2))
