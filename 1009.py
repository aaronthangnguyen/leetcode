# 1009. Complement of Base 10 Integer
# O(1) time, O(1) space


def complement(n: int) -> int:
    x = 1
    while n > x:
        x = 2 * x + 1
    return x ^ n


if __name__ == "__main__":
    print(complement(5))
