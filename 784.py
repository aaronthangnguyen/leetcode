# Letter Case Permutation
# O(2^n * n) time, O(2^n * n) space

from typing import List


def letter_case_permutation(stg: str) -> List[str]:
    def dfs(i: int = 0, path: str = "") -> None:
        if i == n:
            res.append(path)
            return
        if not stg[i].isalpha():
            dfs(i + 1, path + stg[i])
        else:
            dfs(i + 1, path + stg[i].lower())
            dfs(i + 1, path + stg[i].upper())

    n = len(stg)
    res = []
    dfs()
    return res


def letter_case_permutation2(stg: str) -> List[str]:
    res = [""]
    for chr in stg:
        for i in range(len(res)):
            if chr.isalpha():
                res.append(res[i] + chr.lower())
                res[i] = res[i] + chr.lower()
            else:
                res[i] = res[i] + chr
    return res


if __name__ == "__main__":
    print(letter_case_permutation("a1b2"))
    print(letter_case_permutation2("a1b2"))
