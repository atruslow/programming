from typing import Optional, List, Iterator


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        return _generate(self)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Given an integer x, return true if x is palindrome integer.
        """

        l1_sum = sum(val * 10 ** i for i, val in enumerate(_generate(l1)))
        l2_sum = sum(val * 10 ** i for i, val in enumerate(_generate(l2)))

        list_sum = l1_sum + l2_sum

        return _gen_list((int(i) for i in reversed(str(list_sum))))


def _gen_list(array: Iterator[int]) -> ListNode:
    array = iter(array)

    first_node = ListNode(val=next(array))
    last_node = first_node

    for item in array:

        last_node.next = ListNode(val=item)
        last_node = last_node.next

    return first_node


def _generate(node):

    i = node
    yield i.val

    while i.next:
        yield i.next.val
        i = i.next


def _run(*args, **kwargs):
    return Solution().addTwoNumbers(*args, **kwargs)


def test_works():

    assert list(_run(_gen_list([2, 4, 3]), _gen_list([5, 6, 4]))) == [7, 0, 8]
    assert list(_run(_gen_list([0]), _gen_list([0]))) == [0]
    assert list(_run(_gen_list([9, 9, 9, 9, 9, 9, 9]), _gen_list([9, 9, 9, 9]))) == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]


def test_fail():

    assert list(_run(_gen_list([2, 4, 9]), _gen_list([5, 6, 4, 9]))) == [7, 0, 4, 0, 1]
