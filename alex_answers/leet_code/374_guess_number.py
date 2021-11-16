from statistics import mean
from typing import List
from heapq import merge

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

GUESS_VALUE = 0


def guess(num: int) -> int:
    if num == GUESS_VALUE:
        return 0

    return 1 if GUESS_VALUE > num else -1


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked.

        Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

        You call a pre-defined API int guess(int num), which returns 3 possible results:

        -1: The number I picked is lower than your guess (i.e. pick < num).
        1: The number I picked is higher than your guess (i.e. pick > num).
        0: The number I picked is equal to your guess (i.e. pick == num).
        Return the number that I picked.
        """

        current_guess = n
        floor = 0
        celling = n

        while result := guess(current_guess):

            if result < 0:
                # Number is lower
                celling = current_guess
                current_guess = current_guess - ((celling - floor) / 2)
            else:
                # Number is higher
                floor = current_guess
                current_guess = current_guess + ((celling - floor) / 2)

        return int(current_guess)


def _run(*args, **kwargs):
    return Solution().guessNumber(*args, **kwargs)


def test_works():
    global GUESS_VALUE
    GUESS_VALUE = 6
    assert _run(10) == 6


def test_works_again():
    global GUESS_VALUE
    GUESS_VALUE = 11
    assert _run(20) == 11


def test_works_a_third_time():
    global GUESS_VALUE
    GUESS_VALUE = 100
    assert _run(1000) == 100


def test_works_a_fourth_time():
    global GUESS_VALUE
    GUESS_VALUE = 1
    assert _run(1) == 1
