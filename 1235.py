from typing import List
from bisect import bisect_left
from functools import lru_cache


def maximum_profit_in_job_scheduling(
    starts: List[int], ends: List[int], profits: List[int]
) -> int:
    jobs = sorted(zip(starts, ends, profits))
    starts.sort()

    def find_next(arr: List[int], target: int):
        return bisect_left(arr, target)

    @lru_cache(None)
    def rec(i: int):
        if i == len(starts):
            return 0
        j = find_next(starts, jobs[i][1])
        one = jobs[i][2] + rec(j)
        two = rec(i + 1)
        return max(one, two)

    return rec(0)


if __name__ == "__main__":
    starts = [1, 2, 3, 3]
    ends = [1, 2, 3, 3]
    profits = [50, 10, 40, 70]
    assert maximum_profit_in_job_scheduling(starts, ends, profits) == 120

    starts = [1, 2, 3, 4, 6]
    ends = [3, 5, 10, 6, 9]
    profits = [20, 20, 100, 70, 60]
    assert maximum_profit_in_job_scheduling(starts, ends, profits) == 150
