# 33. Search in Rotated Sorted Array
# O(log n) time, O(1) space

from typing import List


def search(numbers: List[int], target: int) -> int:
    l, r = 0, len(numbers) - 1
    while l <= r:
        m = l + (r - l) // 2
        if numbers[m] == target:
            return m
        elif numbers[l] <= numbers[m]:
            if numbers[l] <= target < numbers[m]:
                r = m - 1
            else:
                l = m + 1
        else:  # numbers[l] > numbers[m]
            if numbers[m] < target <= numbers[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
