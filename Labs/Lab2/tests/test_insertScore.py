from utilities.insertScore import insertScore

def testInsertScore():
    score_list = [1,2,3,4,5,6,7]
    score_list = insertScore(score_list, 2, 5)
    assert score_list == [1,2,5,3,4,5,6,7]

    try:
        insertScore(score_list, 2, 5)
        assert True
    except ValueError:
        assert False

    try:
        insertScore(score_list, 1, 11)
        assert False
    except ValueError:
        assert True

    try:
        insertScore(score_list, 0, 120)
        assert False
    except ValueError:
        assert True

testInsertScore()