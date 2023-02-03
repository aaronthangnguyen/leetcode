# 22. Generate Parentheses
# O(2^(2 * n) time, O(n) space

from typing import List


def generate_parentheses(n: int) -> List[str]:
    def backtrack(left: int = 0, right: int = 0) -> None:
        if len(path) == n * 2:
            res.append("".join(path))

        if left < n:
            path.append("(")
            backtrack(left + 1, right)
            path.pop()

        if right < left:
            path.append(")")
            backtrack(left, right + 1)
            path.pop()

    res, path = [], []
    backtrack()
    return res


def generate_parentheses2(n: int) -> List[str]:
    def backtrack(left: int = 0, right: int = 0, path: str = "") -> None:
        if len(path) == n * 2:
            res.append(path)

        if left < n:
            backtrack(left + 1, right, path + "(")

        if right < left:
            backtrack(left, right + 1, path + ")")

    res = []
    backtrack()
    return res


if __name__ == "__main__":
    print(generate_parentheses(3))
    print(generate_parentheses(1))
