import unittest

def rotate_matrix(matrix: list) -> list:
    if len(matrix) != len(matrix[0]):
        return "only works for matricies with equal number of rows & columns"

    m = len(matrix[0])
    out = [[0] * len(matrix[0]) for i in range(len(matrix))]

    for i in range(0, m):
        for j in range(0, m):
            print("NEW IDX:{}{} OLD IDX:{}{} VALUE: {}".format(j, m-1-i, i, j, matrix[i][j]))
            out[j][m-1-i] = matrix[i][j]

    return out

class TestRotateMatrix(unittest.TestCase):
    def test_rotate_matrix_ok(self):
        case = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        want = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        got = rotate_matrix(case)
        self.assertEqual(got, want, "got: '{}' want: '{}'".format(got, want))

if __name__ == '__main__':
    unittest.main()
