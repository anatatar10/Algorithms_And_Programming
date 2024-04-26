import utils.helpers as h
import math
import matplotlib.pyplot as plt


class MyPoint:
    def __init__(self, coord_x, coord_y, color):
        """
        Create a point object with coordinate x, coordinate y and color
        :param coord_x:
        :type coord_x: int
        :param coord_y:
        :type coord_y: int
        :param color:
        :type color: str
        """
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        if h.checkColor(color) == 1:
            self.__color = color
        else:
            raise ValueError("color is incorrect!")

    # getter functions for the properties
    # the name of the function becomes the name of the property
    @property
    def coord_x(self):
        """
        Get the x coordinate of the point
        :return:
        :rtype: int
        """
        return self.__coord_x

    @property
    def coord_y(self):
        """
        Get the y coordinate of the point
        :return:
        :rtype: int
        """
        return self.__coord_y

    @property
    def color(self):
        """
        Get the color of the point
        :return:
        :rtype: str
        """
        return self.__color

    # setter functions for the properties

    @coord_x.setter
    def coord_x(self, newCoord_x):
        """
        Set the x coord of the point
        :return:
        :rtype: int
        """
        self.__coord_x = newCoord_x

    @coord_y.setter
    def coord_y(self, newCoord_y):
        """
        Set the y coord of the point
        :return:
        :rtype: int
        """
        self.__coord_y = newCoord_y

    @color.setter
    def color(self, newColor):
        """
        Set the color of the point
        :return:
        :rtype: str
        """
        if h.checkColor(newColor) == 1:
            self.__color = newColor
        else:
            raise ValueError("color is incorrect!")

    def __str__(self):
        """
        Return the string representation of the point.
        :return:
        :rtype:
        """

        return f"Point({self.__coord_x}, {self.__coord_y}) of color {self.__color}"

    def __repr__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Check if two points objects are equal by comparing their properties
        :param other:
        :type other: MyPoint
        :return:
        :rtype: bool
        """
        return self.__coord_x == other.__coord_x and self.__coord_y == other.__coord_y and self.__color == other.__color


class PointRepository:
    def __init__(self, initialPoints=None):
        """
        Creating a repository containing points
        """

        self.__list_of_points = []
        if initialPoints is not None:
            # check if the coordinates are unique
            for point in initialPoints:
                if isinstance(point, MyPoint):
                    self.__list_of_points.append(point)

    def addPoint(self, coord_x, coord_y, color):
        """
        ex. 1
        Add a new point to the repository
        :param coord_x:
        :type coord_x: int
        :param coord_y:
        :type coord_y: int
        :param color:
        :type color: str
        :return:
        :rtype:
        """
        if h.checkColor(color) == 1:
            self.__list_of_points.append(MyPoint(coord_x, coord_y, color))
        else:
            raise ValueError("Point not added. The accepted colors are: ‘red’, ‘green’, ‘blue’, ‘yellow’ and ‘magenta’")

    def getPoints(self):
        """
        ex. 2
        Get all points from the repository.
        Return a copy of the list! Otherwise, the user can change the content of the list.
        :return:
        :rtype: list
        """
        return self.__list_of_points[:]

    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of point
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__list_of_points) or 0 == index == len(self.__list_of_points)

    def __isLengthCorrect(self, length):
        """
        Check if the given length is correct
        :param length:
        :type length: int
        :return:
        :rtype: bool
        """
        if length > 0:
            return 1
        else:
            return 0

    def getPointAtGivenIndex(self, index):
        """
        ex3: Get a point at a given index
        :param index:
        :type index: int
        :return:
        :rtype: MyPoint
        """
        if self.__isIndexCorrect(index):
            return self.__list_of_points[index]
        else:
            raise IndexError("Index invalid")

    def __getitem__(self, index):
        return self.getPointAtGivenIndex(index)

    def getPointsGivenColor(self, color):
        """
        ex 4: Get all points of a given color
        :param color:
        :type color: str
        :return:
        :rtype: MyPoint
        """
        listPointsColor = []
        if h.checkColor(color):
            for point in self.__list_of_points:
                if point.color == color:
                    listPointsColor.append(point)
            return listPointsColor
        else:
            raise ValueError("Color is incorrect!")

    def getPointsInsideGivenSquare(self, coord_x, coord_y, length):
        """
        ex 5: Get all points that are inside a given square (up-left corner and length given)
        :param coord_x:
        :type coord_x: int
        :param coord_y:
        :type coord_y: int
        :param length:
        :type length: int
        :return:
        :rtype: list
        """
        listPointsSquare = []
        if self.__isLengthCorrect(length) == 1:
            for point in self.__list_of_points:
                if coord_x <= point.coord_x <= coord_x + length and coord_y - length <= point.coord_y <= coord_y:
                    listPointsSquare.append(point)
            return listPointsSquare
        else:
            raise ValueError("Length needs to be positive")

    def getMinimumDistance(self):
        """
        ex.6.: Get the minimum distance between two given points
        :param coord_x:
        :type coord_x: float
        :param coord_y:
        :type coord_y: float
        :return distance
        :rtype: float
        """
        if len(self.__list_of_points) >= 2:
            point0 = self.__list_of_points[0]
            point1 = self.__list_of_points[1]
            initialDistance = math.sqrt(((point1.coord_x - point0.coord_x) ** 2) + ((point1.coord_y - point0.coord_y) ** 2))
            for i in range(len(self.__list_of_points)):
                for j in range(i+1, len(self.__list_of_points)):
                    distance = (((self.__list_of_points[i].coord_x - self.__list_of_points[j].coord_x) ** 2) + ((self.__list_of_points[i].coord_y - self.__list_of_points[j].coord_y) ** 2)) ** (1 / 2)
                    if distance < initialDistance:
                        initialDistance = distance
            return initialDistance
        else:
            raise ValueError("There are not at least 2 points")


    def updatePointAtGivenIndex(self, index, coord_x, coord_y, color):
        """
        ex 7: Update a point at a given index
        :param index:
        :type index: int
        :param coord_x:
        :type coord_x: int
        :param coord_y:
        :type coord_y: int
        :param color:
        :type color: str
        :return:
        :rtype: MyPoint
        """
        if self.__isIndexCorrect(index):
            if h.checkColor(color) == 1:
                point = self.__list_of_points[index]
                point.coord_x = coord_x
                point.coord_y = coord_y
                point.color = color
                return point
            else:
                raise ValueError("Color not accepted")
        else:
            raise IndexError("Index invalid")


    def deletePointAtGivenIndex(self, index):
        """
        ex 8: Delete a point by index
        :param index:
        :type index: int
        :return:
        :rtype: MyPoint
        """
        if self.__isIndexCorrect(index):
            del self.__list_of_points[index]
        else:
            raise IndexError("Index is not correct")

    def deletePointsInsideGivenSquare(self, coord_x, coord_y, length):
        """
        ex 9: Delete all points that are inside a given square
        :param coord_x:
        :type coord_x: int
        :param coord_y:
        :type coord_y: int
        :param length:
        :type length: int
        :return:
        :rtype: MyPoint
        """
        if self.__isLengthCorrect(length) == 1:
            index = len(self.__list_of_points) - 1
            while index >= 0:
                point = self.__list_of_points[index]
                if coord_x <= point.coord_x <= coord_x + length and coord_y - length <= point.coord_y <= coord_y:
                    del self.__list_of_points[index]
                index -= 1
        else:
            raise ValueError("Length needs to be positive")

    def numberOfPointGivenColor(self, color):
        """
        ex 14: Get the number of points of a given color
        :param color:
        :ty[e color: str
        :return:
        :rtype: int
        """
        count = 0
        if h.checkColor(color):
            for point in self.__list_of_points:
                if point.color == color:
                    count = count + 1
            return count
        else:
            raise ValueError("Color is not valid")

    def shiftPointsYAxis(self, range):
        """
        ex 17: Shift all points on the y axis
        :param range:
        :type range: int
        :return:
        :rtype: MyPoint
        """
        index = len(self.__list_of_points) - 1

        while index >= 0:
            point = self.__list_of_points[index]
            point.coord_y = point.coord_y + range
            index -= 1

    def deletePoints(self, coord_x, coord_y, distance):
        """
        ex 20: Delete all points within a certain distance from a given point
        :param coord_x:
        :type coord_x: int
        :param coord_y:
        :type coord_y: int
        :param distance:
        :type distance: int
        :return:
        :rtype MyPoint
        """
        index = len(self.__list_of_points) - 1
        if distance > 0:
            while index >= 0:
                point = self.__list_of_points[index]
                distance1 = math.sqrt(((point.coord_x - coord_x) ** 2) + ((point.coord_y - coord_y) ** 2))
                if distance1 <= distance:
                    del self.__list_of_points[index]
                index -= 1
        else:
            raise ValueError("Distance is not valid. It has to be a positive value.")

    def getPointCount(self):
        """
        Get the number of points in the repository
        :return:
        :rtype: int
        """
        return len(self.__list_of_points)

    def plotAllPoints(self):
        """
        Plot all points in a chart (using library matplotlib)
        :return:
        """
        listX = []
        listY = []
        listColor = []
        for point in self.__list_of_points:
            listX.append(point.coord_x)
            listY.append(point.coord_y)
            listColor.append(point.color)
        plt.scatter(listX, listY, c = listColor)
        plt.show()


    def __repr__(self):
        """
        Return the string representation of the class.
        :return:
        :rtype: str
        """
        if len(self.__list_of_points) == 0:
            return "No points!"
        else:
            str_repr = ""
            for point in self.__list_of_points:
                str_repr += str(point) + "\n"
            return str_repr

if __name__ == "__main__":
    repo = PointRepository([MyPoint(5, 6, 'red'), MyPoint(3, 2, "blue"), MyPoint(2, 0, "yellow"), MyPoint(7, 7, "green"), MyPoint(6, 4, "magenta")])

    repo.getMinimumDistance()





