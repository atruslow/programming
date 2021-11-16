
from typing import List


def max_area(height: List[int]) -> int:

    alpha = 0
    beta = len(height)-1
    _max_area = 0

    while alpha < beta:
        first, second = height[alpha], height[beta]

        _max_area = max(_max_area, _compute_area(first, second, beta-alpha))

        if first < second:
            alpha += 1
        else:
            beta -= 1

    return _max_area


def _compute_area(wall_one, wall_two, distance):

    return min(wall_one, wall_two) * distance


def test_example_one():

    assert max_area([1,8,6,2,5,4,8,3,7]) == 49


def test_example_two():

    assert max_area([1,1]) == 1


def test_example_three():

    assert max_area([4,3,2,1,4]) == 16


def test_example_four():

    assert max_area([1,2,1]) == 2



