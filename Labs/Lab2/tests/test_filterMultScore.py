from utilities.filterMultScore import filterMultScore

def testFilterMultScore():
    score_list = [2, 4, 6, 5, 8, 10, 3]
    score_list = filterMultScore(score_list, 2)
    assert score_list == [2, 4, 6, 8, 10]

    try:
        newList = filterMultScore(score_list, 2)
        if newList == score_list:
            assert True
    except ValueError:
        assert False

    try:
        newList = filterMultScore(score_list, 3)
        if newList != score_list:
            assert True
    except ValueError:
        assert False

    try:
        newList = filterMultScore(score_list, 19)
        if newList != score_list:
            assert True
    except ValueError:
        assert False

testFilterMultScore()