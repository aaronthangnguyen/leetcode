# 378. Kth Smallest Element in a Sorted Matrix
# O(n * log (max - min)) time, O(1) space

from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    def count_less_or_equal(x: int) -> int:
        res = 0
        c = n - 1

        for r in range(n):
            while c >= 0 and matrix[r][c] > x:
                c -= 1
            res += c + 1

        return res

    n = len(matrix)
    l, r = matrix[0][0], matrix[-1][-1]
    res = -1

    while l <= r:
        m = (l + r) // 2
        if count_less_or_equal(m) >= k:
            r = m - 1
        else:
            l = m + 1

    return l


if __name__ == "__main__":
    print(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
