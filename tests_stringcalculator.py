import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add("1;2;312"), 9)


if __name__ == '__main__':
    unittest.main()
