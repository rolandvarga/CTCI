import re
import unittest

def is_unique(string: str) -> bool:
    unique = []
    for s in string:
        if s in unique:
            return False
        else:
            unique.append(s)
    return True

def is_unique_recursion(string: str) -> bool:
    if len(string) >= 1:
        return is_unique_recursion(string[1:]) and (string[0] not in string[1:])
    return True

def is_unique_simple(string: str) -> bool:
    return len(string) == len(set(string))

def is_permutation(string_A, string_B: str) -> bool:
    list_A = list(string_A)
    list_B = list(string_B)
    list_A.sort()
    list_B.sort()

    if len(list_A) == len(list_B):
        return list_A == list_B
    return False

def URLify(string: str) -> str:
    string = re.sub(r"\s+", "%20", string)
    last = string.rfind("%20")

    return string[:last] + string[last:].replace("%20", "")

class TestUnique(unittest.TestCase):
    def test_is_unique(self):
        cases = [
            ("asdf", True),
            ("aabc", False),
            ("qwer", True),
        ]

        for string, want in cases:
            got = is_unique(string)
            self.assertEqual(got, want, "should be able to tell if unique")

    def test_is_unique_recursion(self):
        cases = [
            ("asdf", True),
            ("aabc", False),
            ("qwer", True),
        ]

        for string, want in cases:
            got = is_unique_recursion(string)
            self.assertEqual(got, want, "should be able to tell if unique")

class TestPermutation(unittest.TestCase):
    def test_permutation_ok(self):
        cases = [
            ("asd", "dsa", True),
            ("aabc", "qwer", False),
            ("qwer", "q", False),
            ("1234", "3421", True),
        ]

        for a, b, want in cases:
            got = is_permutation(a, b)
            self.assertEqual(got, want, "should know if permutation")

class TestURLify(unittest.TestCase):
    def test_url_ok(self):
        cases = [
            ("Mr John Smith     ", "Mr%20John%20Smith"),
        ]

        for string, want in cases:
            got = URLify(string)
            self.assertEqual(got, want, "got: '{}' want: '{}'".format(got, want))


if __name__ == '__main__':
    unittest.main()
