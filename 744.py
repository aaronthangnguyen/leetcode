# 744. Find Smallest Letter Greater than Target
# O(log n) time, O(1) space

from typing import List


def find_smallest_letter_greater_than_target(letters: List[str], target: str) -> str:
    if not (letters[0] <= target < letters[-1]):
        return letters[0]

    l, r = 0, len(letters) - 1
    while l <= r:
        m = l + (r - l) // 2
        if letters[m] <= target:
            l = m + 1
        else:
            r = m - 1

    return letters[l]
