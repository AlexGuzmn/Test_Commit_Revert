import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add("321453"), 18)


if __name__ == '__main__':
    unittest.main()
