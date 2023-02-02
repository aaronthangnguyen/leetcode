# 90. Subsets II
# O(n * 2^n) time, O(n) space
from typing import List


def subset_ii(numbers: List[int]) -> List[List[int]]:
    def backtrack(i: int) -> None:
        res.append(path[:])
        for j in range(i, n):
            if j > i and numbers[j] == numbers[j - 1]:
                continue
            path.append(numbers[j])
            backtrack(j + 1)
            path.pop()
        return

    numbers.sort()
    n = len(numbers)

    res, path = [], []
    backtrack(0)

    return res
