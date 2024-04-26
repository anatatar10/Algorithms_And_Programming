from utilities.removeScoreFromTo import removeScoreFromTo

def testRemoveScoreFromTo():
    score_list = [3, 4, 5, 6, 7, 8, 9, 10]
    removeScoreFromTo(score_list, 0, 3)
    assert score_list == [7, 8, 9, 10]

    try:
        removeScoreFromTo(score_list, 0, 3)
        assert True
    except ValueError:
        assert False

    try:
        removeScoreFromTo(score_list, 11, 100)
        assert False
    except ValueError:
        assert True

    try:
        removeScoreFromTo(score_list, 3, 11)
        assert False
    except ValueError:
        assert True

testRemoveScoreFromTo()