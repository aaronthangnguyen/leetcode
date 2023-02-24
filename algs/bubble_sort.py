# Bubble Sort
# O(n^2) time, O(1) space

from typing import List


def bubble_sort(numbers: List[int]):
    n = len(numbers)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


if __name__ == "__main__":
    numbers = [2, 1, 3, 9, 4, 5, 8, 7, 6]
    bubble_sort(numbers)
    print(numbers)
