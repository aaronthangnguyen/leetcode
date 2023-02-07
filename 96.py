# 96. Unique Binary Search Trees
# O(n^2) time, O(n) space


def unique_bst(n: int) -> int:
    res = [0] * (n + 1)
    res[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            res[i] += res[j] * res[i - j - 1]

    return res[n]


if __name__ == "__main__":
    print(unique_bst(3))
