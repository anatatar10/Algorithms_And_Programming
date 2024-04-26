from utilities.avgScoreFromTo import avgScoreFromTo

def testAvgScoreFromTo():
    score_list = [8, 4, 4, 10]
    average = avgScoreFromTo(score_list, 1, 3)
    assert average == 6

    try:
        average = avgScoreFromTo(score_list, 0, 0)
        if average == 8:
            assert True
    except ValueError:
        assert False

    try:
        avgScoreFromTo(score_list, 40, 200)
        assert False
    except ValueError:
        assert True

    try:
        avgScoreFromTo(score_list, 29, 1)
        assert False
    except ValueError:
        assert True

testAvgScoreFromTo()