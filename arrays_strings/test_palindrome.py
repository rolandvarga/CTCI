import unittest

def is_palindrome_permutation(string: str) -> bool:
    chars = {}
    for s in string.replace(" ", "").lower():
        if not s in chars:
            chars[s] = 1
        else:
            chars[s] += 1

    total = sum([value % 2 for value in chars.values()])
    return total <= 1


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome_permutation_ok(self):
        cases = [
            ("Tact Coa", True),
            ("racecar", True),
            ("code", False),
            ("aab", True),
            ("carerac", True),
        ]

        for c, want in cases:
            got = is_palindrome_permutation(c)
            self.assertEqual(got, want, "got: '{}' want: '{}'".format(got, want))

if __name__ == '__main__':
    unittest.main()
