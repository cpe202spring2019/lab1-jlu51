import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #Checks for the exception
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    #Tests if list is empty
        self.assertEqual(max_list_iter([]), None)

    #Tests if list exists
        tlist = [5, 2, 4, 6, 1]
        self.assertEqual(max_list_iter(tlist), 6)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        list_val = [1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        # self.assertEqual(bin_search(4, low, len(list_val)-1, list_val), 3)
        # self.assertEqual(bin_search(1, low, len(list_val) - 1, list_val), 0)
        # self.assertEqual(bin_search(0, low, len(list_val) - 1, list_val), None)

        #Checks for the exception
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(5, low, high, tlist)

        #Not in the list
        self.assertEqual(bin_search(0, low, len(list_val) - 1, list_val), None)

        #Left side
        self.assertEqual(bin_search(4, low, len(list_val)-1, list_val), 3)

        #Right side
        self.assertEqual(bin_search(9, low, len(list_val)-1, list_val), 6)

        #Right side
        self.assertEqual(bin_search(9, low, len(list_val)-1, list_val), 6)

if __name__ == "__main__":
        unittest.main()

