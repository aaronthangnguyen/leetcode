from typing import List


def lower_bound(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


def upper_bound(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return high


if __name__ == "__main__":
    arr = [1, 3, 3, 3, 5, 6]
    target = 3
    print(f"Lower bound: {lower_bound(arr, target)}")
    print(f"Upper bound: {upper_bound(arr, target)}")
