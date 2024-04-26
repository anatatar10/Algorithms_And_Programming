from domain.MyPoint import *

def testCreatePoint():
    try:
        MyPoint(1, 2, "purple")
        assert False
    except ValueError:
        assert True

def testGettersAndSetters():
    p = MyPoint(1, 2, 'blue')
    assert p.coord_x == 1
    assert p.coord_y == 2
    assert p.color == 'blue'

    p.coord_x = 2
    assert p.coord_x == 2
    p.coord_y = 3
    assert p.coord_y == 3
    p.color = 'red'
    assert p.color == 'red'
    try:
        # testing if error is raised when color is not correct
        p.color = 'purple'
        assert False
    except ValueError:
        assert True

    p.coord_x = 3
    assert p.coord_x == 3
    p.coord_y = 4
    assert p.coord_y == 4
    p.color = 'yellow'
    assert p.color == 'yellow'
    try:
        # testing if error is raised when color is not correct
        p.color = 'brown'
        assert False
    except ValueError:
        assert True

def testCreatePointRepository():
    pr = PointRepository()
    assert pr.getPointCount() == 0
    pr = PointRepository([MyPoint(1, 2, 'blue')])
    assert pr.getPointCount() == 1
    pr = PointRepository([MyPoint(1, 2, 'blue'), MyPoint(3, 3, 'red')])
    assert pr.getPointCount() == 2
    pr = PointRepository([MyPoint(1, 2, 'blue'), MyPoint(3, 3, 'red'), MyPoint(-3, -2, "green")])
    assert pr.getPointCount() == 3

def testAddPoint():
    pr = PointRepository()
    assert pr.getPointCount() == 0
    pr = PointRepository([MyPoint(1, 2, 'blue')])
    assert pr.getPointCount() == 1
    try:
        # testing if error is raised when inserting an invalid color
        pr.addPoint(2, 3, 'purple')
        assert False
    except ValueError:
        assert True
    try:
        pr.addPoint(3, 4, 'green')
        assert True
    except ValueError:
        assert False
    try:
        # testing if error is raised when inserting an invalid color
        pr.addPoint(4, 5, 'brown')
        assert False
    except ValueError:
        assert True

def testGetPointAtGivenIndex():
    pr = PointRepository([MyPoint(1, 2, 'blue'), MyPoint(3, 3, 'red')])

    assert str(pr.getPointAtGivenIndex(0)) == "Point(1, 2) of color blue"
    assert str(pr[0]) == "Point(1, 2) of color blue"
    assert str(pr.getPointAtGivenIndex(1)) == "Point(3, 3) of color red"
    assert str(pr[1]) == "Point(3, 3) of color red"

    try:
        # testing if error is raised when index does not exist
        pr.getPointAtGivenIndex(2)
        assert False
    except IndexError:
        assert True

    try:
        # testing if error is raised when index does not exist
        print(pr[2])
        assert False
    except IndexError:
        assert True

def testGetPointsGivenColor():
    pr = PointRepository([MyPoint(1, 2, 'blue'), MyPoint(3, 3, 'red')])

    assert str(pr.getPointsGivenColor('blue')) == "[Point(1, 2) of color blue]"
    assert str(pr.getPointsGivenColor('red')) == "[Point(3, 3) of color red]"

    try:
        # testing if error is raised when inserting an invalid color
        if str(pr.getPointsGivenColor('purple')) == []:
            assert False
    except ValueError:
        assert True

    try:
        # testing if error is raised when there isn't yellow in the list
        if str(pr.getPointsGivenColor('yellow')) == []:
            assert False
    except ValueError:
        assert True

def testGetPointsInsideGivenSquare():
    pr = PointRepository(
        [MyPoint(5, 6, 'red'), MyPoint(3, 2, "blue"), MyPoint(2, 0, "yellow"), MyPoint(7, 7, "green"),
         MyPoint(6, 4, "magenta")])

    assert str(pr.getPointsInsideGivenSquare(3,8,5)) == "[Point(5, 6) of color red, Point(7, 7) of color green, Point(6, 4) of color magenta]"
    assert str(pr.getPointsInsideGivenSquare(1,10,4)) == "[Point(5, 6) of color red]"

    try:
        if str(pr.getPointsInsideGivenSquare(0,0,1)) == []:
            assert False
    except ValueError:
        assert True

    try:
        if str(pr.getPointsInsideGivenSquare(-1,-5,-1)) == []:
            assert False
    except ValueError:
        assert True

def testGetMinimumDistance():
    pr = PointRepository(
        [MyPoint(5, 6, 'red'), MyPoint(3, 2, "blue"), MyPoint(2, 0, "yellow"), MyPoint(7, 7, "green"),
         MyPoint(6, 4, "magenta")])

    #assert pr.getMinimumDistance() == 6.4031242374328485


def testUpdatePointAtGivenIndex():
    pr = PointRepository(
        [MyPoint(5, 6, 'red'), MyPoint(3, 2, "blue"), MyPoint(2, 0, "yellow"), MyPoint(7, 7, "green"),
         MyPoint(6, 4, "magenta")])

    assert str(pr.updatePointAtGivenIndex(0, 10, 11, "yellow")) == "Point(10, 11) of color yellow"
    assert str(pr.updatePointAtGivenIndex(3, 1, 1, "magenta")) == "Point(1, 1) of color magenta"

    try:
        # testing if error is raised when inserting an invalid index
        pr.updatePointAtGivenIndex(-2,1,1,"green")
        assert False
    except IndexError:
        assert True

    try:
        # testing if error is raised when inserting an index which does not exist
        pr.updatePointAtGivenIndex(10,1,1,"blue")
        assert False
    except IndexError:
        assert True

def testDeletePointAtGivenIndex():
    pr = PointRepository([MyPoint(1, 2, 'blue'), MyPoint(3, 3, 'red')])

    pr.deletePointAtGivenIndex(0)
    assert pr.getPointCount() == 1
    assert str(pr.getPointAtGivenIndex(0)) == "Point(3, 3) of color red"

    try:
        # testing if error is raised when inserting an index which does not exist
        pr.deletePointAtGivenIndex(1)
        assert False
    except IndexError:
        assert True

    try:
        pr.deletePointAtGivenIndex(0)
        assert True
    except IndexError:
        assert False

def testDeletePointsInsideGivenSquare():
    pr = PointRepository([MyPoint(5, 6, 'red'), MyPoint(3, 2, "blue")])

    assert pr.getPointCount() == 2
    pr.deletePointsInsideGivenSquare(1, 10, 5)
    assert pr.getPointCount() == 1
    assert str(pr.getPointAtGivenIndex(0)) == "Point(3, 2) of color blue"

def testNumberOfPointGivenColor():
    pr = PointRepository(
        [MyPoint(5, 6, 'red'), MyPoint(3, 2, "blue"), MyPoint(2, 0, "yellow"), MyPoint(7, 7, "green"),
         MyPoint(6, 4, "red")])

    assert pr.numberOfPointGivenColor("red") == 2
    assert pr.numberOfPointGivenColor("blue") == 1
    assert pr.numberOfPointGivenColor("magenta") == 0

    try:
        if pr.numberOfPointGivenColor("magenta") == 0:
            assert True
    except ValueError:
        assert False

def testShiftPointsYAxis():
    pr = PointRepository([MyPoint(5, 6, 'red'), MyPoint(1,2, 'blue')])

    pr.shiftPointsYAxis(5)
    assert str(pr.getPointAtGivenIndex(0)) == "Point(5, 11) of color red"
    assert str(pr.getPointAtGivenIndex(1)) == "Point(1, 7) of color blue"

    try:
        pr.shiftPointsYAxis(-1)
        assert True
    except ValueError:
        assert False

    try:
        pr.shiftPointsYAxis(10)
        assert True
    except ValueError:
        assert False

def testDeletePointsAtDistance():
    pr = PointRepository([MyPoint(4, 4, 'red'), MyPoint(6, 6, "blue")])

    pr.deletePoints(3, 3, 1.4142135623731)
    assert pr.getPointCount() == 1
    assert str(pr.getPointAtGivenIndex(0)) == "Point(6, 6) of color blue"

    try:
        # testing if error is raised when inserting an invalid distance
        pr.deletePoints(10,10, -3)
        assert False
    except ValueError:
        assert True

    try:
        pr.deletePoints(8, 8, 1)
        assert True
    except ValueError:
        assert False


def runAllTests():
    testCreatePoint()
    testGettersAndSetters()
    testCreatePointRepository()
    testAddPoint()
    testGetPointAtGivenIndex()
    testGetPointsGivenColor()
    testGetPointsInsideGivenSquare()
    testGetMinimumDistance()
    testUpdatePointAtGivenIndex()
    testDeletePointAtGivenIndex()
    testDeletePointsInsideGivenSquare()
    testNumberOfPointGivenColor()
    testShiftPointsYAxis()
    testDeletePointsAtDistance()

runAllTests()