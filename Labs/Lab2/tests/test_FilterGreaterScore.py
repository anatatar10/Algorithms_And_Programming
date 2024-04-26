from utilities.filterGreaterScore import filterGreaterScore

def testFilterGreaterScore():
    score_list = [1, 2, 3, 4, 5, 6, 7, 8]
    newList = filterGreaterScore(score_list, 3)
    assert newList == [4,5,6,7,8]

    try:
        newList1 = filterGreaterScore(score_list, 3)
        if newList1 == [4,5,6,7,8]:
            assert True
    except ValueError:
        assert False

    try:
        newList1 = filterGreaterScore(score_list, 11)
        if newList1 == [4,5,6,7,8]:
            assert False
    except ValueError:
        assert True
    
    try:
        newList1 = filterGreaterScore(score_list, 1)
        if newList1 == [4,5,6,7,8]:
            assert False
    except ValueError:
        assert True

testFilterGreaterScore()