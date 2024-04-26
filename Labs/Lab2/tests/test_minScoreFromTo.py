from utilities.minScoreFromTo import minScoreFromTo

def testMinScoreFromTo():
    score_list = [7, 2, 9, 3, 8, 4, 6]
    MINI = minScoreFromTo(score_list, 1, 5)
    assert MINI == 2

    try:
        minScoreFromTo(score_list, 1, 5)
        assert True
    except ValueError:
        assert False

    try:
        minScoreFromTo(score_list, 11, 'abc')
        assert False
    except ValueError:
        assert True

    try:
        minScoreFromTo(score_list, 3, 11)
        assert False
    except ValueError:
        assert True

testMinScoreFromTo()