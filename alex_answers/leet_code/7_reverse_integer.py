class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        """

        is_neg = x < 0
        rev_x = int("".join(reversed(str(abs(x)))))

        if rev_x > 2_147_483_647:
            return 0

        return rev_x if not is_neg else rev_x * -1


def _run(*args, **kwargs):
    return Solution().reverse(*args, **kwargs)


def test_works():

    assert _run(123) == 321
    assert _run(-123) == -321
    assert _run(120) == 21
    assert _run(0) == 0


def test_fail():

    assert _run(1534236469) == 0
