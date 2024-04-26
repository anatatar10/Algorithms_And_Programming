from utils.helpers import *


def testCheckColor():
    assert not checkColor("purple")
    assert not checkColor("brown")
    assert checkColor("green")


def runAllTests():
    testCheckColor()