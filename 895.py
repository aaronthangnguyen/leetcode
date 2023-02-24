# 895. Maximum Frequency Stack

from collections import defaultdict
from heapq import heappush, heappop


# O(1) time, O(n) space
class FreqStack:
    def __init__(self):
        self.stacks = []
        self.freqs = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        freq = self.freqs[val]
        if freq > len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[freq - 1].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.freqs[val] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return val


# O(log n) time, O(n) space
class FreqStack2:
    def __init__(self):
        self.heap = []
        self.freqs = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        freq = self.freqs[val]
        heappush(self.heap, (-freq, -self.index, val))
        self.index += 1

    def pop(self):
        *_, val = heappop(self.heap)
        self.freqs[val] -= 1
        return val


if __name__ == "__main__":
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(7)
    fs.push(4)
    fs.push(5)
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())

    fs2 = FreqStack()
    fs2.push(5)
    fs2.push(7)
    fs2.push(7)
    fs2.push(4)
    fs2.push(5)
    print(fs2.pop())
    print(fs2.pop())
    print(fs2.pop())
    print(fs2.pop())
