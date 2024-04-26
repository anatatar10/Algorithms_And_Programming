from utilities.lessScore import lessScore

def testLessScore():
    score_list = [10, 5, 8, 3, 1, 9, 7, 6]
    newList = lessScore(score_list, 6)
    assert newList == [1, 3, 4]

    try:
        if lessScore(score_list, 6) != newList:
            assert True
    except ValueError:
        assert False

    try:
        if lessScore(score_list, 1) != newList:
            assert True
    except ValueError:
        assert False

    try:
        lessScore(score_list, 11)
        assert False
    except ValueError:
        assert True

testLessScore()