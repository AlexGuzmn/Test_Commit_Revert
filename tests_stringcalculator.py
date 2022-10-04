import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add("31;2;45"), 15)


if __name__ == '__main__':
    unittest.main()
