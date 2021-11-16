from typing import List


def binary_search(nums: List[int], target: int) -> int:

    max_index = len(nums) - 1
    guess_index = max_index // 2
    floor = 0
    celling = max_index

    if nums[0] > target or target > nums[-1]:
        return -1

    while True:

        guess_value = nums[guess_index]

        if guess_value == target:
            return guess_index

        item_not_exist = nums[guess_index-1] < target < guess_value

        if item_not_exist:
            return -1

        if guess_value < target:
            floor = guess_index
            guess_index = ((celling - guess_index) // 2) + guess_index
            if guess_index == floor:
                guess_index += 1

        elif guess_value > target:
            celling = guess_index
            guess_index = guess_index - (guess_index - floor)


def test_works():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_second_case():
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_negative_out_of_bounds():
    assert binary_search([5], -5)


def test_end_of_array():
    assert binary_search([2, 5], 5)


def test_end_of_array_two():
    assert binary_search([-1, 0, 5], -1) == 0


def test_next_to_end_of_array():

    assert binary_search([-1,0,3,5,9,12], 0) == 1


if __name__ == "__main__":

    test_end_of_array()

    import pytest

    pytest.main([__file__])
