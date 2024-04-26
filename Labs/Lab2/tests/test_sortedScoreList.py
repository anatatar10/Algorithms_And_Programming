from utilities.sortedScoreList import sortedScoreList

def testSortedScoreList():
    score_list = [5, 2, 8, 1, 7, 3, 9, 4]
    newList = sortedScoreList(score_list)
    assert newList == [1, 2, 3, 4, 5, 7, 8, 9]

    try:
        if sortedScoreList(score_list) == newList:
            assert True
    except ValueError:
        assert False

    try:
        if sortedScoreList(score_list) != newList:
            assert False
    except ValueError:
        assert True

    """try:
        sortedScoreList(score_list)
        assert True
    except ValueError:
        assert False"""

testSortedScoreList()