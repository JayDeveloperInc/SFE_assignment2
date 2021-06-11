import unittest
from case_conversion import swap
from expanded_form import expanded_form
class assm_tests(unittest.TestCase):
    def test_swap(self):
        test_string = "mine"
        test_num = 11

        result = swap(test_string, test_num)

        self.assertNotEqual(result, test_string)

    def test_expanded_form(self):
        test_num = -11
        result = expanded_form(test_num)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
