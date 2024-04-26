from utilities.addScore import addScore

def testAddScore():
    score_list = []
    addScore(score_list, 1)
    assert score_list == [1]

    try:
        addScore(score_list, 1)
        assert True
    except ValueError:
        assert False

    try:
        addScore(score_list, 231)
        assert False
    except ValueError:
        assert True

    try:
        addScore(score_list, 199)
        assert False
    except ValueError:
        assert True

testAddScore()