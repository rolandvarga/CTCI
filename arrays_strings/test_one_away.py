import unittest

def one_char_replaced(string_a, string_b: str) -> bool:
        found = False
        for i in range(len(string_a)):
            if string_a[i] != string_b[i]:
                if found:
                    return False
                else:
                    found = True
        return True

def count_inserted_chars(string_a, string_b: str) -> int:
    j = 0
    count = 0
    for i in range(len(string_a)):
        if string_a[i] != string_b[j]:
            count += 1
            j += 1
    return count % 2


def is_one_away(string_a, string_b: str) -> bool:
    if len(string_a) == len(string_b):
        return one_char_replaced(string_a, string_b)
    elif len(string_a) + 1 == len(string_b):
        return count_inserted_chars(string_a, string_b) <= 1
    elif len(string_b) + 1 == len(string_a):
        return count_inserted_chars(string_b, string_a) <= 1

    return False


class TestOneAway(unittest.TestCase):
    def test_is_one_away_ok(self):
        cases = [
            ("pale", "ple", True),
            ("pales", "pale", True),
            ("pale", "bale", True),
            ("pale", "bake", False),
        ]

        for a, b, want in cases:
            got = is_one_away(a, b)
            self.assertEqual(got, want, "got: '{}' want: '{}'".format(got, want))

if __name__ == '__main__':
    unittest.main()
