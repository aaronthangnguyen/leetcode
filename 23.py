# 23. Merge k Sorted Lists
# O(_) time, O(_) space

from typing import List, Optional, Self
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = [(node.val, i) for i, node in enumerate(lists) if node]
    heapify(heap)

    stn = prev = ListNode()

    while heap:
        _, i = heappop(heap)
        node = lists[i]
        prev.next = node
        prev = prev.next
        if node and node.next:
            heappush(heap, (node.next.val, i))
            lists[i] = lists[i].next

    return stn.next


def new_list(numbers: List[int]) -> Optional[ListNode]:
    stn = prv = ListNode()
    for number in numbers:
        prv.next = ListNode(number)
        prv = prv.next
    return stn.next


def print_list(lst: Optional[ListNode]):
    sep = ""
    while lst:
        print(f"{sep}{lst.val}", end="")
        lst = lst.next
        sep = "->"
    print("")


if __name__ == "__main__":
    lst1 = new_list([1, 4, 5])
    lst2 = new_list([1, 3, 4])
    lst3 = new_list([2, 6])
    print_list(merge([lst1, lst2, lst3]))
