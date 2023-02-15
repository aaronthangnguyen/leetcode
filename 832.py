# 832. Flipping an Image
# O(n^2) time, O(1) space

from typing import List
from copy import deepcopy


def flip_invert(image: List[List[int]]) -> List[List[int]]:
    n = len(image)
    for r in range(n):
        image[r].reverse()
        for c in range(n):
            image[r][c] ^= 1
    return image


def flip_invert2(image: List[List[int]]) -> List[List[int]]:
    n = len(image)
    for row in image:
        for c in range((n + 1) // 2):
            row[c], row[~c] = row[~c] ^ 1, row[c] ^ 1
    return image


if __name__ == "__main__":
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(flip_invert(deepcopy(image)))
    print(flip_invert2(deepcopy(image)))
