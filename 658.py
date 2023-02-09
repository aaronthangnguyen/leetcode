# 658. Find K Closest Elements
# O(log(n - k) + k) time, O(1) space

from typing import List


def find(numbers: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(numbers) - k - 1
    while l <= r:  # O(n - k)
        m = l + (r - l) // 2
        if x - numbers[m] > numbers[m + k] - x:
            l = m + 1
        else:
            r = m - 1
    return numbers[l : l + k]  # O(k)


if __name__ == "__main__":
    print(find([1, 2, 3, 4, 5], 4, 3))
