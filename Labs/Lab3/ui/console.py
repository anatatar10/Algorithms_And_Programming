from domain import MyPoint as p
from utils.readCommand import readCommand
from utils.readCoordX import readCoordX
from utils.readCoordY import readCoordY
from utils.readColor import readColor
from utils.readIndex import readIndex
from utils.readLength import readLength


def dataExamples():
    repo = p.PointRepository(
        [p.MyPoint(5, 6, 'red'), p.MyPoint(3, 2, "blue")])
    print(repo)

    print("ex.1.")
    print("add a new point: Point(10, 10) of color blue")
    repo.addPoint(10, 10, "blue")
    print(repo)
    print("add a new point: Point(1, 1) of color yellow")
    repo.addPoint(1, 1, "yellow")
    print(repo)
    print("add a new point: Point(0, 4) of color magenta")
    repo.addPoint(0, 4, "magenta")
    print(repo)
    print("add a new point: Point(2, 7) of color brown")
    try:
        repo.addPoint(2,7, "brown")
    except ValueError as ve:
        print (ve)
    print(repo)
    print("add a new point: Point(8, 3) of color black")
    try:
        repo.addPoint(8, 3, "black")
    except ValueError as ve:
        print(ve)
    print(repo)
    print("add a new point: Point(5, 5) of color yellow")
    repo.addPoint(5, 5, "blue")
    print(repo)
    print("add a new point: Point(3, 1) of color red")
    repo.addPoint(3, 1, "yellow")
    print(repo)
    print("add a new point: Point(7, 3) of color green")
    repo.addPoint(7, 3, "green")
    print(repo)
    print("add a new point: Point(3, -2) of color magenta")
    repo.addPoint(3, -2, "magenta")
    print(repo)
    print("add a new point: Point(-4, -6) of color green")
    repo.addPoint(-4, -6, "green")

    print("ex.2.")
    print("Points in the repo as list:", repo.getPoints())

    print("ex.3.")
    print(repo)
    print(f"point at index 4 is {repo[4]}")
    print(f"point at index 0 is {repo[0]}")
    print(f"point at index 3 is {repo[3]}")
    try:
        print("point at index 15 is", end=" ")
        repo.getPointAtGivenIndex(15)
    except IndexError:
        print("not defined in the repository!")
    try:
        print("point at index -2 is", end=" ")
        repo.getPointAtGivenIndex(-2)
    except IndexError:
        print("not defined in the repository!")
    try:
        print("point at index 100 is", end=" ")
        repo.getPointAtGivenIndex(100)
    except IndexError:
        print("not defined in the repository!")
    print(f"point at index 1 is {repo[1]}")
    print(f"point at index 5 is {repo[5]}")
    print(f"point at index 2 is {repo[2]}")

    print("ex.4")
    print("Points of color blue in the repo as list: ", repo.getPointsGivenColor("blue"))
    print("Points of color red in the repo as list: ", repo.getPointsGivenColor("red"))
    print("Points of color yellow in the repo as list: ", repo.getPointsGivenColor("yellow"))
    print("Points of color green in the repo as list: ", repo.getPointsGivenColor("green"))
    print("Points of color magenta in the repo as list: ", repo.getPointsGivenColor("magenta"))
    try:
        print("Points of color brown", end=" ")
        repo.getPointsGivenColor('brown')
    except ValueError:
        print("not defined in the repository!")
    try:
        print("Points of color white", end=" ")
        repo.getPointsGivenColor('white')
    except ValueError:
        print("not defined in the repository!")
    try:
        print("Points of color purple", end=" ")
        repo.getPointsGivenColor('purple')
    except ValueError:
        print("not defined in the repository!")
    try:
        print("Points of color cyan", end=" ")
        repo.getPointsGivenColor('cyan')
    except ValueError:
        print("not defined in the repository!")
    try:
        print("Points of color orange", end=" ")
        repo.getPointsGivenColor('orange')
    except ValueError:
        print("not defined in the repository!")

    print("ex.5.")
    print(repo)
    print("Points inside a square having the up-left corner at (5,5) and length 5 are: ", repo.getPointsInsideGivenSquare(5,5,5))
    print("Points inside a square having the up-left corner at (10,10) and length 1 are: ", repo.getPointsInsideGivenSquare(10, 10, 1))
    print("Points inside a square having the up-left corner at (0,0) and length 1 are: ", repo.getPointsInsideGivenSquare(0, 0, 1))
    try:
        print("Points inside a square having the up-left corner at (3, 4) and length -2 are none.", end=" ")
        repo.getPointsInsideGivenSquare(3, 4, -2)
    except ValueError:
        print("Length has to be a positive value greater than 0")
    try:
        print("Points inside a square having the up-left corner at (1, 8) and length -5 are none.", end=" ")
        repo.getPointsInsideGivenSquare(1, 8, -5)
    except ValueError:
        print("Length has to be a positive value greater than 0")
    print("Points inside a square having the up-left corner at (1,2) and length 7 are: ",repo.getPointsInsideGivenSquare(1, 2, 7))
    print("Points inside a square having the up-left corner at (-5,-5) and length 3 are: ",repo.getPointsInsideGivenSquare(-5, -5, 3))
    print("Points inside a square having the up-left corner at (0,3) and length 4 are: ", repo.getPointsInsideGivenSquare(0, 3, 4))
    try:
        print("Points inside a square having the up-left corner at (-10, 1) and length -5 are none.", end=" ")
        repo.getPointsInsideGivenSquare(-10, 1, -5)
    except ValueError:
        print("Length has to be a positive value greater than 0")
    try:
        print("Points inside a square having the up-left corner at (1, 8) and length 0 are none.", end=" ")
        repo.getPointsInsideGivenSquare(1, 8, 0)
    except ValueError:
        print("Length has to be a positive value greater than 0")

    print("ex.6.")
    print(repo)
    print("The minimum distance between the points in the repo is:", repo.getMinimumDistance())


    print("ex.7.")
    print(repo)
    print(f"update point at index 4 with (1,3) of color blue.")
    repo.updatePointAtGivenIndex(4, 1,3, 'blue')
    print(f"now the point at index 4 is {repo[4]}")
    try:
        print(f"update point at index 50 with (10,10) and color green.")
        repo.updatePointAtGivenIndex(50, 10, 10, 'green')
    except IndexError:
        print("Index 50 does not exist in the list.")
    try:
        print(f"update point at index 0 with (10,8) and color purple.")
        repo.updatePointAtGivenIndex(0, 10, 8, 'purple')
    except ValueError:
        print("Purple is not accepted.")
    try:
        print(f"update point at index -2 with (1,4) and color blue")
        repo.updatePointAtGivenIndex(-2, 1, 4, 'blue')
    except IndexError:
        print("Index -2 does not exist in the list")
    print(f"update point at index 3 with (12, -3) of color yellow.")
    repo.updatePointAtGivenIndex(3, 12, -3, 'blue')
    print(f"now the point at index 3 is {repo[3]}")
    print(f"update point at index 0 with (3, -3) of color red.")
    repo.updatePointAtGivenIndex(0, 3, -3, 'red')
    print(f"now the point at index 0 is {repo[0]}")
    try:
        print(f"update point at index 2 with (10,11) and color brown.")
        repo.updatePointAtGivenIndex(2, 10, 11, 'brown')
    except ValueError:
        print("Brown is not accepted.")
    try:
        print(f"update point at index 5 with (0,-3) and color cyan.")
        repo.updatePointAtGivenIndex(5, 0, -3, 'cyan')
    except ValueError:
        print("Cyan is not accepted.")
    print(f"update point at index 6 with 3, 1) of color magenta.")
    repo.updatePointAtGivenIndex(6, 3, 1, 'magenta')
    print(f"now the point at index 6 is {repo[6]}")
    print(f"update point at index 7 with (7, 4) of color red.")
    repo.updatePointAtGivenIndex(7, 7, 4, 'red')
    print(f"now the point at index 7 is {repo[7]}")

    print("ex.8.")
    print(repo)
    print(f"The number of points in the repository is {repo.getPointCount()}")
    print(f"delete point at index 4")
    repo.deletePointAtGivenIndex(4)
    print(f"now the point at index 4 is {repo[4]}")
    print(f"The number of points in the repository is {repo.getPointCount()}")
    try:
        print(f"delete point at index 50")
        repo.deletePointAtGivenIndex(50)
    except IndexError:
        print("Index 50 does not exist!")
        print(f"The number of points in the repository is {repo.getPointCount()}")
    try:
        print(f"delete point at index -3")
        repo.deletePointAtGivenIndex(-3)
    except IndexError:
        print("Index -3 does not exist!")
        print(f"The number of points in the repository is {repo.getPointCount()}")
    try:
        print(f"delete point at index 50")
        repo.deletePointAtGivenIndex(24)
    except IndexError:
        print("Index 24 does not exist!")
        print(f"The number of points in the repository is {repo.getPointCount()}")
    try:
        print(f"delete point at index 12")
        repo.deletePointAtGivenIndex(12)
    except IndexError:
        print("Index 12 does not exist!")
        print(f"The number of points in the repository is {repo.getPointCount()}")
    print(f"delete point at index 0")
    repo.deletePointAtGivenIndex(0)
    print(f"now the point at index 0 is {repo[0]}")
    print(f"The number of points in the repository is {repo.getPointCount()}")
    print(f"delete point at index 6")
    repo.deletePointAtGivenIndex(6)
    print(f"now the point at index 6 is {repo[6]}")
    print(f"The number of points in the repository is {repo.getPointCount()}")
    print(f"delete point at index 4")
    repo.deletePointAtGivenIndex(4)
    print(f"now the point at index 4 is {repo[4]}")
    print(f"The number of points in the repository is {repo.getPointCount()}")
    print(f"delete point at index 3")
    repo.deletePointAtGivenIndex(3)
    print(f"now the point at index 3 is {repo[3]}")
    print(f"The number of points in the repository is {repo.getPointCount()}")
    print(f"delete point at index 2")
    repo.deletePointAtGivenIndex(2)
    print(f"now the point at index 4 is {repo[2]}")
    print(f"The number of points in the repository is {repo.getPointCount()}")

    print("ex.9.")
    print(repo)
    print("Delete points inside a square having the up-left corner at (5,5) and length 5")
    repo.deletePointsInsideGivenSquare(5,5,5)
    print(repo)
    try:
        print("Delete points inside a square having the up-left corner at (-10, 1) and length -5.", end=" ")
        repo.getPointsInsideGivenSquare(-10, 1, -5)
    except ValueError:
        print("Length has to be a positive value greater than 0")
    print("Delete points inside a square having the up-left corner at (0,0) and length 1")
    repo.deletePointsInsideGivenSquare(0, 0, 1)
    print(repo)

    print("ex.10.")
    print(repo)
    print("Plot all the remaining points in a chart")
    repo.plotAllPoints()


def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - add a new point")
    print(" 2 - get all points")
    print(" 3 - get point at given index")
    print(" 4 - get all points of given color")
    print(" 5 - get all points that are inside a given square")
    print(" 6 - get the minimum distance between two points")
    print(" 7 - update a point at a given index")
    print(" 8 - delete a point by index")
    print(" 9 - delete all points that are inside a given square")
    print("10 - plot all points in a chart")
    print("11 - get the number of points of a given color")
    print("12 - shift all points on the y axis")
    print("13 - delete all points within a certain distance from a given point")

def start():
    print()
    pointRepo = p.PointRepository()
    printMenu()
    command = None
    while command != 0: # while True
        try:  # catches all conversion errors
            command = readCommand()
            if command == -2:
                dataExamples()
            elif command == -1:
                printMenu()
            elif command == 0:
                print("program ended successfully")
            elif command == 1:
                print("You have chosen to add a new point to the repository.")
                coord_x = readCoordX()
                coord_y = readCoordY()
                color = readColor()
                try:
                    pointRepo.addPoint(coord_x, coord_y, color)
                    print(pointRepo)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                print("You have chosen to get all the points")
                print(pointRepo.getPoints())
            elif command == 3:
                print("You have chosen to get a point at a given index.")
                index = readIndex()
                try:
                    print(f"The point at index {index} is {pointRepo[index]}")
                except IndexError as ie:
                    print(ie)
            elif command == 4:
                print("You have chosen to get all the points of a given color.")
                color = readColor()
                try:
                    print(pointRepo.getPointsGivenColor(color))
                except ValueError as ve:
                    print(ve)
            elif command == 5:
                print("You have chosen to get all points inside a given square")
                coord_x = readCoordX()
                coord_y = readCoordY()
                length = readLength()
                try:
                    print(pointRepo.getPointsInsideGivenSquare(coord_x, coord_y, length))
                except ValueError as ve:
                    print(ve)
            elif command == 6:
                print("You have chosen to get the minimum distance between two points")
                coord_x = int(input("x coordinate 1st point: "))
                coord_y = int(input("y coordinate 1st point: "))
                coord_x1 = int(input("x coordinate 2nd point: "))
                coord_y1 = int(input("y coordinate 2nd point: "))
                print(pointRepo.getMinimumDistance())
            elif command == 7:
                print("You have chosen to update a point at a given index")
                index = readIndex()
                coord_x = int(input("New x coordinate: "))
                coord_y = int(input("New y coordinate: "))
                color = input("New color: ")
                try:
                    pointRepo.updatePointAtGivenIndex(index, coord_x, coord_y, color)
                    print(f"The point at index {index} was updated.")
                    print(f"After update:\t{pointRepo[index]}")
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)
            elif command == 8:
                print("You have chosen to delete a point by index")
                index = readIndex()
                try:
                    pointRepo.deletePointAtGivenIndex(index)
                    print(f"The point at index {index} is")
                except IndexError as ie:
                    print(ie)
            elif command == 9:
                print("You have chosen to delete all points that are inside a given square")
                coord_x = readCoordX()
                coord_y = readCoordY()
                length = readLength()
                try:
                    print(pointRepo.deletePointsInsideGivenSquare(coord_x, coord_y, length))
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)
            elif command == 10:
                print("You have chosen to plot all the points in a chart")
                print(pointRepo.plotAllPoints())
            elif command == 11:
                print("You have chosen to get the number of points of a given color")
                color = readColor()
                try:
                    print(pointRepo.numberOfPointGivenColor(color))
                except ValueError as ve:
                    print(ve)
            elif command == 12:
                print("You have chosen to shift all points on the y axis")
                range = int(input("Enter the range: "))
                pointRepo.shiftPointsYAxis(range)
                print(pointRepo)
            elif command == 13:
                print("You have chosen to delete all points within a certain distance from a given point")
                coord_x = readCoordX()
                coord_y = readCoordY()
                distance = int(input("Enter the distance: "))
                try:
                    pointRepo.deletePoints(coord_x, coord_y, distance)
                    print(pointRepo)
                except ValueError as ve:
                    print(ve)
            else:
                print("invalid command")
        except ValueError:
            print("invalid type entered!")