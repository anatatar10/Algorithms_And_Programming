from utilities.undo import undo

def testUndo():
    score_list = []
    undo(score_list, 5)
    assert score_list == [5]

    try:
        undo(score_list, 6)
        assert True
    except ValueError:
        assert False

    try:
        undo(score_list, 11)
        assert False
    except ValueError:
        assert True

    try:
        undo(score_list, 'a')
        assert False
    except ValueError:
        assert True

#testUndo()