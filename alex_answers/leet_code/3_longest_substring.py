from itertools import permutations, combinations


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        """
        if not s:
            return 0

        chars_set = set(s)
        max_unique_len = len(chars_set)

        if max_unique_len == len(s):
            return len(s)

        if max_unique_len == 1:
            return 1

        for n_gram_len in range(max_unique_len, 1, -1):

            for combo in generate_ngrams(s, n_gram_len):

                if len(set(combo)) == len(combo):
                    return len(combo)

        return 1


def generate_ngrams(s, n):

    ngrams = zip(*[s[i:] for i in range(n)])

    return ["".join(ngram) for ngram in ngrams]


def _run(*args, **kwargs):
    return Solution().lengthOfLongestSubstring(*args, **kwargs)


def test_works():

    assert _run("abcabcbb") == 3
    assert _run("bbbbb") == 1
    assert _run("pwwkew") == 3


def test_fail():

    assert _run("") == 0
    assert _run("aab") == 2
    assert _run("dvdf") == 3