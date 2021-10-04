from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.
        """

        value__index = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):

            compliment = target - num

            try:
                if i != value__index[compliment]:
                    return [i, value__index[compliment]]
            except KeyError:
                pass


def test_base_case():

    assert sorted(Solution().twoSum([2, 7, 11, 15], 9)) == [0, 1]


def test_base_case_two():

    assert sorted(Solution().twoSum([3, 2, 4], 6)) == [1, 2]


def test_base_case_three():

    assert sorted(Solution().twoSum([3, 3], 6)) == [0, 1]


def test_fail_case():

    assert sorted(Solution().twoSum([0, 4, 3, 0], 0)) == [0, 3]


def test_fail_case_negative():

    assert sorted(Solution().twoSum([-1, -2, -3, -4, -5], -8)) == [2, 4]
