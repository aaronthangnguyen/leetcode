# 136. Single Number
# O(n) time, O(1) space

from typing import List
from functools import reduce


def single_number(numbers: List[int]) -> int:
    res = 0
    for number in numbers:
        res ^= number
    return res


def single_number2(numbers: List[int]) -> int:
    return reduce(lambda number, res: res ^ number, numbers)


if __name__ == "__main__":
    print(single_number([2, 2, 1]))
    print(single_number2([2, 2, 1]))
