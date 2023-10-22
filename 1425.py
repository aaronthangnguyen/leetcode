from typing import List
import heapq


def constrained_subsequence_sum(nums: List[int], k: int) -> int:
    if not nums:
        return 0

    res = nums[0]
    heap = [(-nums[0], 0)]

    for i in range(1, len(nums)):
        while i - heap[0][1] > k:
            heapq.heappop(heap)
        curr = max(nums[i], nums[i] - heap[0][0])
        heapq.heappush(heap, (-curr, i))
        res = max(res, curr)

    return res


if __name__ == "__main__":
    nums = [10, 2, -10, 5, 20]
    k = 2
    assert constrained_subsequence_sum([10, 2, -10, 5, 20], 2) == 37
    assert constrained_subsequence_sum([-1, -2, -3], 1) == -1
    assert constrained_subsequence_sum([10, -2, -10, -5, 20], 2) == 23
    print("Passed!")
