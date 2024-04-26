from utilities.removeScore import removeScore

def testRemoveScore():
    score_list = [8, 2, 5, 1, 9, 10, 7]
    removeScore(score_list, 3)
    assert score_list == [8, 2, 5, 9, 10, 7]

    try:
        removeScore(score_list, 3)
        assert True
    except ValueError:
        assert False

    try:
        removeScore(score_list, 11)
        assert False
    except ValueError:
        assert True

    try:
        removeScore(score_list, 100)
        assert False
    except ValueError:
        assert True

testRemoveScore()