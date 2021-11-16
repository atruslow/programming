from typing import List
from collections import deque


def total_fruit(fruits: List[int]) -> int:

    max_length = 0
    seen_fruit = deque(maxlen=2)
    pointer_one = 0

    for i, fruit in enumerate(fruits):

        if fruit in seen_fruit:
            max_length = max(max_length, i+1 - pointer_one)
            seen_fruit.append(fruit)
            continue

        seen_fruit.append(fruit)

        if len(seen_fruit) == 2:

            segment = fruits[pointer_one:i]

            if len(set(segment)) == 2:
                max_length = max(max_length, len(segment))

            while any(i not in seen_fruit for i in segment):
                pointer_one += 1
                segment = fruits[pointer_one:i]

        max_length = max(max_length, i+1 - pointer_one)

    return max_length


def test_example_one():

    assert total_fruit([1, 2, 1]) == 3


def test_example_two():

    assert total_fruit([0, 1, 2, 2]) == 3


def test_example_three():

    assert total_fruit([1, 2, 3, 2, 2]) == 4


def test_example_four():

    assert total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5


def test_example_five():

    assert total_fruit([0]) == 1


def test_example_six():

    assert total_fruit([1,0]) == 2


def test_example_seven():

    assert total_fruit([3,3,3,1,4]) == 4


def test_example_eight():

    assert total_fruit([0,1,6,6,4,4,6]) == 5


def test_example_nine():

    assert total_fruit([1,0,1,4,1,4,1,2,3]) == 5