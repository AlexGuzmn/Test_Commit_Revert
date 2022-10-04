import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add("5,61-9;382,1"), 26)


if __name__ == '__main__':
    unittest.main()
