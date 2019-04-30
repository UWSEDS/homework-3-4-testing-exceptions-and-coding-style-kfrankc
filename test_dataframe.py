from subprocess import check_output
import unittest


class MyTest(unittest.TestCase):
    def test_expected_correct_col(self):
        out = check_output(["python3", "dataframe.py", "data.csv"])
        self.assertEqual(
            out, b'Congratulations, input dataframe passes all checks.\n')

    def test_expected_correct_types(self):
        out = check_output(["python3", "dataframe.py", "data.csv"])
        self.assertEqual(
            out, b'Congratulations, input dataframe passes all checks.\n')

    def test_expected_1_row(self):
        out = check_output(["python3", "dataframe.py", "data.csv"])
        self.assertEqual(
            out, b'Congratulations, input dataframe passes all checks.\n')

    def test_incorrect_col(self):
        out = check_output(["python3", "dataframe.py",
                           "data_incorrect_col.csv"])
        self.assertEqual(
            out, b'Input DataFrame does not contain the expected columns.\n')

    def test_incorrect_col(self):
        out = check_output(["python3", "dataframe.py",
                           "data_float.csv"])
        self.assertEqual(
            out, b'Input DataFrame does not contain the correct data type.\n')
if __name__ == '__main__':
    unittest.main()
