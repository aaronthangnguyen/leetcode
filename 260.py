# 260. Single Number III
# O(n) time, O(1) space

from typing import List


def single_number_iii(numbers: List[int]) -> List[int]:
    bitmask = 0
    for number in numbers:
        bitmask ^= number

    diff = bitmask & (-bitmask)

    x = 0
    for number in numbers:
        if number & diff:
            x ^= number

    return [x, bitmask ^ x]


if __name__ == "__main__":
    print(single_number_iii([1, 2, 1, 3, 2, 5]))
