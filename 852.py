# 852. Peak Index in a Mountain Array
# O(log n) time, O(1) space

from typing import List


def peak_index(numbers: List[int]) -> int:
    l, r = 0, len(numbers) - 1

    while l <= r:
        m = l + (r - l) // 2
        if numbers[m] <= numbers[m + 1]:
            l = m + 1
        else:
            r = m - 1
    return l


if __name__ == "__main__":
    print(peak_index([0, 10, 5, 2]))
