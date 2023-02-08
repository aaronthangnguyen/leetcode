# 704. Binary Search
# O(log n) time, O(1) space

from typing import List


def binary_search(numbers: List[int], target: int) -> int:
    l, r = 0, len(numbers) - 1
    while l <= r:
        m = l + (r - l) // 2
        if numbers[m] == target:
            return m
        elif numbers[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))
