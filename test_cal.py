# CS362_Winter21
# Class Activity
# Program: test_cal.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that demonstrates pass and fail conditions for the program.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 test_cal.py
###########################################################################

import unittest
import activity_cal as cal

class CalculatorTests(unittest.TestCase):
    def test_type_true(self):
        self.assertTrue(type(cal.cal_add(4, 3)) is int)
        self.assertTrue(type(cal.cal_sub(4, 3)) is int)
        self.assertTrue(type(cal.cal_mul(4, 3)) is int)
        self.assertTrue(type(cal.cal_div(4, 3)) is int) # FAIL
    def test_equal(self):
        self.assertEqual(cal.cal_add(4, 3), 7)
        self.assertEqual(cal.cal_sub(4, 3), 1)
        self.assertEqual(cal.cal_mul(4, 3), 12)
        self.assertEqual(cal.cal_div(4, 3), 1.3) # FAIL
    def test_greater(self):
        self.assertGreater(cal.cal_add(3, 4), 0)
        self.assertGreater(cal.cal_sub(3, 4), 0) # FAIL
        self.assertGreater(cal.cal_mul(3, 4), 0)
        self.assertGreater(cal.cal_div(3, 4), 0)
    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            cal.cal_div(4, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)