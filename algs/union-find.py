from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

    def print(self):
        print("root: ", end="")
        print(self.root)


def find_i(par: List[int], a: int) -> int:
    parent = par[a]
    while parent != a:
        par[a] = par[parent]
        a = parent
        parent = par[parent]
    return parent


def find_r(par: List[int], a: int) -> int:
    if a == par[a]:
        return a
    par[a] = find_r(par, par[a])
    return par[a]


if __name__ == "__main__":
    par_i = [0, 0, 1, 2, 3]
    print(find_i(par_i, 4))
    print(par_i)
    par_r = [0, 0, 1, 2, 3]
    print(find_r(par_r, 4))
    print(par_r)
