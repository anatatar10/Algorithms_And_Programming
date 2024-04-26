from utilities.sortedScoreListHigher import sortedScoreListHigher

def testSortedScoreListHigher():
    score_list = [10,9,8,7,6,5,4,3,2,1]
    newList = sortedScoreListHigher(score_list, 3)
    assert newList == [0, 1, 2, 3, 4, 5, 6]

    try:
        if sortedScoreListHigher(score_list, 2) == newList:
            assert True
    except ValueError:
        assert False

    try:
        if sortedScoreListHigher(score_list, 9) != newList:
            assert True
    except ValueError:
        assert False

    try:
        sortedScoreListHigher(score_list, 100)
        assert False
    except ValueError:
        assert True

testSortedScoreListHigher()