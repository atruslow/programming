from statistics import mean
from typing import List
from heapq import merge


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).
        """

        merged_arrays = list(merge(nums1, nums2))
        array_len = len(merged_arrays)
        half_point = int(array_len/2)

        if array_len % 2 == 1:
            return merged_arrays[half_point]

        return mean([merged_arrays[half_point - 1], merged_arrays[half_point]])


def _run(*args, **kwargs):
    return Solution().findMedianSortedArrays(*args, **kwargs)


def test_works():

    assert _run([1, 3], [2]) == 2.0
    assert _run([1, 2], [3, 4]) == 2.5
    assert _run([0, 0], [0, 0]) == 0.0
    assert _run([], [1]) == 1.0
    assert _run([2], []) == 2.0




