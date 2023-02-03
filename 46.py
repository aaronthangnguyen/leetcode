# 46. Permutations
# _ time, _ space
from typing import List


def permutations(numbers: List[int]) -> List[List[int]]:
    def swap(a: int, b: int) -> None:
        numbers[a], numbers[b] = numbers[b], numbers[a]

    def backtrack(p: int) -> None:
        if p == n:
            res.append(numbers[:])
            return
        for i in range(p, n):
            swap(p, i)
            backtrack(p + 1)
            swap(p, i)

    n = len(numbers)
    res = []
    backtrack(0)
    return res


if __name__ == "__main__":
    numbers = [1, 2, 3]
    print(permutations(numbers))
