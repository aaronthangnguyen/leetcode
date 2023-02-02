# 78. Subsets
# O(n * 2^n) time, O(n) space
from typing import List


def subsets(numbers: List[int]) -> List[List[int]]:
    def dfs(i: int) -> None:
        res.append(path[:])
        for j in range(i, n):
            path.append(numbers[j])
            dfs(j + 1)
            path.pop()
        return

    n = len(numbers)
    res = []
    path = []
    dfs(0)
    return res
