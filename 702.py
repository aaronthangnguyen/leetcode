# 702. Search in a Sorted Array of Unknown Size
# O(log n) time, O(1) space

from typing import List


class ArrayReader:
    def __init__(self, array: List[int]):
        self.array = array[:]
        self.last_index = len(array) - 1

    def get(self, index: int) -> int:
        if index > self.last_index:
            return 2 ^ 31 - 1
        return self.array[index]


def search(reader: "ArrayReader", target: int) -> int:
    l, r = 0, target - reader.get(0)

    while l <= r:
        m = l + (r - l) // 2
        val = reader.get(m)
        if val == target:
            return m
        elif val < target:
            l = m + 1
        else:
            r = m - 1

    return -1


if __name__ == "__main__":
    reader = ArrayReader([-1, 0, 3, 5, 9, 12])
    print(search(reader, 9))
