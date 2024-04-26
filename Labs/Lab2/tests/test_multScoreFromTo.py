from utilities.multScoreFromTo import multScoreFromTo

def testMultScoreFromTo():
    score_list = [6, 3, 8, 7, 2, 9, 4, 10]
    newList = multScoreFromTo(score_list, 3, 0, 6)
    assert newList == [6, 3, 9]

    try:
        multScoreFromTo(score_list, 3, 0, 6)
        assert True
    except ValueError:
        assert False

    try:
        newList1 = multScoreFromTo(score_list, 2, 11, 100)
        if newList1 != newList:
            assert False
    except ValueError:
        assert True

    try:
        newList1 = multScoreFromTo(score_list, 12, 3, 4)
        if newList1 != newList:
            assert False
    except ValueError:
        assert True

testMultScoreFromTo()