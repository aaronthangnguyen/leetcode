# 95. Unique Binary Search Trees II
# O(2^n) time, O(log n) space

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def unique_bst(n: int):
    def generate_trees(start: int, end: int):
        if start > end:
            return [None]

        trees = []
        for i in range(start, end + 1):
            left_trees = generate_trees(start, i - 1)
            right_trees = generate_trees(i + 1, end)

            for left in left_trees:
                for right in right_trees:
                    tree = TreeNode(i)
                    tree.left = left
                    tree.right = right
                    trees.append(tree)

        return trees

    return generate_trees(1, n) if n else []


if __name__ == "__main__":
    unique_bst(3)
