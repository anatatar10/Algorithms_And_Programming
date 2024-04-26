from unittest import TestCase
from utils import helpersCheckColor as hC
from utils import helpersCheckType as hT

class HelperTestClass(TestCase):
    def testCheckColor(self):
        self.assertTrue(hC.checkColour('r'))
        self.assertEqual(hC.checkColour('y'), True)
        self.assertTrue(hC.checkColour('b'))
        self.assertFalse(hC.checkColour('o'))
        self.assertFalse(hC.checkColour('w'))

    def testCheckType(self):
        self.assertTrue(hT.checkType(1))
        self.assertTrue(hT.checkType(2))
        self.assertEqual(hT.checkType(3), True)
        self.assertFalse(hT.checkType(2.5))
        self.assertFalse(hT.checkType(-3))
