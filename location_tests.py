import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):

        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")


    def test_equal(self):

        #If all values the same
        loc3 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 == loc2

        #If all values are different
        loc3 = Location("SLO", 35.3, -120.7)
        loc2 = Location("San Jose", 0, 0)
        loc3 != loc2

        #If some values are different
        loc3 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 0, 0)
        loc3 != loc2






if __name__ == "__main__":
        unittest.main()
