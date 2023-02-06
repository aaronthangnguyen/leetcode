# 320. Generalized Abbreviation
# O(2^n * n) time, O(n) space
from typing import List


def generalized_abbreviation(word: str) -> List[str]:
    def dfs(p: int = 0, path: str = "") -> None:
        if p == n:
            res.append(path)
            return
        dfs(p + 1, path + word[p])
        if not path or path[-1].isalpha():
            for i in range(p, n):
                dfs(i + 1, path + str(i - p + 1))

    n = len(word)
    res = []
    dfs()
    return res


if __name__ == "__main__":
    print(generalized_abbreviation("word"))
