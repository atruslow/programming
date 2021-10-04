class Solution:
    def isPalindrome(self, x: int) -> int:
        """
        Given an integer x, return true if x is palindrome integer.
        """

        if x < 0:
            return False

        return x == int("".join(reversed(str(x))))


def _run(*args, **kwargs):
    return Solution().isPalindrome(*args, **kwargs)


def test_works():

    assert _run(121) is True
    assert _run(-121) is False
    assert _run(-101) is False


def test_fail():

    assert True
