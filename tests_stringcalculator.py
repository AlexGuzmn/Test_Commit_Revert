import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add("123;12"), 9)


if __name__ == '__main__':
    unittest.main()
