# 1095. Find in Mountain Array
# O(log n) time, O(1) space

from typing import List


class MountainArray:
    def __init__(self, array: List[int]):
        self.array = array

    def get(self, i: int) -> int:
        return self.array[i]

    def length(self):
        return len(self.array)


def peak(array: "MountainArray") -> int:
    n = array.length()
    l, r = 0, n - 1
    while l <= r:
        m = l + (r - l) // 2
        if array.get(m) <= array.get(m + 1):
            l = m + 1
        else:
            r = m - 1
    return l


def find(target: int, array: "MountainArray") -> int:
    n = array.length()

    p = peak(array)
    if array.get(p) == target:
        return p

    # Left of peak
    l, r = 0, p - 1
    while l <= r:
        m = l + (r - l) // 2
        val = array.get(m)
        if val == target:
            return m
        elif val < target:
            l = m + 1
        else:
            r = m - 1

    # Right of peak
    l, r = p + 1, n - 1
    while l <= r:
        m = l + (r - l) // 2
        val = array.get(m)
        if val == target:
            return m
        elif val > target:
            l = m + 1
        else:
            r = m - 1

    return -1


if __name__ == "__main__":
    array = MountainArray([1, 2, 3, 4, 5, 3, 1])
    print(find(3, array))
