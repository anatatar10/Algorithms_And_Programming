from utilities.replaceScore import replaceScore

def testReplaceScore():
    score_list = [8, 3, 5, 1, 9, 10, 4]
    replaceScore(score_list, 0, 7)
    assert score_list == [7, 3, 5, 1, 9, 10, 4]

    try:
        replaceScore(score_list, 0, 7)
        assert True
    except ValueError:
        assert False

    try:
        if replaceScore(score_list, 6, 9) != score_list:
            assert True
    except ValueError:
        assert False

    try:
        replaceScore(score_list, 12, 100)
        assert False
    except ValueError:
        assert True

testReplaceScore()