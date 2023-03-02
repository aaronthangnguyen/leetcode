# 310. Minimum Height Trees
# O(v) time, O(v) space

from typing import List
from collections import defaultdict


def find(n: int, edges: List[List[int]]) -> List[int]:
    if n < 2:
        return [0]

    graph = {node: set() for node in range(n)}
    for node1, node2 in edges:
        graph[node1].add(node2)
        graph[node2].add(node1)

    leaves = []
    for node in range(n):
        if len(graph[node]) == 1:
            leaves.append(node)

    while len(graph) > 2:
        new_leaves = []
        for leaf in leaves:
            next_leaf = graph[leaf].pop()
            del graph[leaf]
            graph[next_leaf].remove(leaf)
            if len(graph[next_leaf]) == 1:
                new_leaves.append(next_leaf)
        leaves = new_leaves

    return leaves


if __name__ == "__main__":
    print(find(4, [[1, 0], [1, 2], [1, 3]]))
