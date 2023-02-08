# 34. Find First and Last Position of Element in Sorted Array
# O(log n) time, O(1) space

from typing import List


def search(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l <= r:
        m = l + (r - l) // 2
        if numbers[m] < target:
            l = m + 1
        else:
            r = m - 1
    left = l

    l, r = 0, len(numbers) - 1
    while l <= r:
        m = l + (r - l) // 2
        if numbers[m] <= target:
            l = m + 1
        else:
            r = m - 1
    right = r
    return [left, right] if left <= right else [-1, -1]


if __name__ == "__main__":
    print(search([5, 7, 7, 8, 8, 10], 8))
