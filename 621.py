# 621. Task Scheduler
# O(n) time, O(1) space

from typing import List
from heapq import heapify


def schedule(tasks: List[str], cooldown: int) -> int:
    """
    Hint: calculate idle time in-between task with max freq
    freqs = {A: 3, B: 3}
    cooldown 2

    A _ _ A _ _ A
    idle = 4

    A B _ A B _ A
    idle = 2
    """
    freqs = [0] * 26
    for task in tasks:
        freqs[ord(task) - ord("A")] += 1
    freqs.sort()

    max_freq = freqs.pop()
    idle = (max_freq - 1) * cooldown

    while freqs and idle > 0:
        idle -= min(max_freq - 1, freqs.pop())
    idle = max(idle, 0)  # idle at least 0
    return idle + len(tasks)


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    print(schedule(tasks, 2))
