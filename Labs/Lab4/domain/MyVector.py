import utils.helpersCheckColor as hC
import utils.helpersCheckType as hT
import matplotlib.pyplot as plt
import numpy as np


class MyVector:
    def __init__(self, nameId, colour, typeVector, values = []):
        """
        Create a vector object with name_id, colour, type and values
        :param nameId:
        :type nameId: int, str
        :param colour:
        :type colour: str
        :param typeVector:
        :type typeVector: int
        :param values:
        :type values: list
        """
        self.__nameId = nameId

        if hC.checkColour(colour) == 1:
            self.__colour = colour
        else:
            raise ValueError("colour is not correct!")

        if hT.checkType(typeVector) == 1:
            self.__typeVector = typeVector
        else:
            raise ValueError("type value is not correct!")

        self.__values = values[:]


    # getter functions for the properties
    # the name of the function becomes the name of the property

    @property
    def nameId(self):
        """
        Get the nameId of the vector
        :return:
        :rtype: int, str
        """
        return self.__nameId

    @property
    def colour(self):
        """
        Get the color of the vector
        :return:
        :rtype: str
        """
        return self.__colour

    @property
    def typeVector(self):
        """
        Get the type of the vector
        :return:
        :rtype: int
        """
        return self.__typeVector

    @property
    def values(self):
        """
        Get the values of the vector
        :return:
        :rtype: list
        """
        return self.__values[:]

    # setter functions for the properties

    @nameId.setter
    def nameId(self, newNameId):

        """
        Set the name_id of the vector
        :return:
        :rtype: int
        """
        self.__nameId = newNameId

    @colour.setter
    def colour(self, newColour):
        """
        Set the color of the vector
        :return:
        :rtype: str
        """
        if hC.checkColour(newColour) == 1:
            self.__colour = newColour
        else:
            raise ValueError("Colour not correct")

    @typeVector.setter
    def typeVector(self, newTypeVector):
        """
        Set the typeVector of the vector
        :return:
        :rtype: int
        """
        if hT.checkType(newTypeVector) == 1:
            self.__typeVector = newTypeVector
        else:
            raise ValueError("Type is not correct")


    @values.setter
    def values(self, newValues = []):
        """
        Set the values of the vector
        :return:
        :rtype: list
        """
        self.__values = newValues[:]

    def __str__(self):
        """
        Return the string representation of the vector.
        :return:
        :rtype:
        """

        return f"MyVector({self.__nameId}, '{self.__colour}', {self.__typeVector}, {self.__values})"

    def __repr__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Check if two vectors objects are equal by comparing their properties
        :param other:
        :type other: MyVector
        :return:
        :rtype: bool
        """
        return self.__nameId == other.__nameId and self.__colour == other.__colour and self.__typeVector == other.__typeVector and self.__values[:] == other.__values[:]

    def addScalarToAVector(self, scalar):
        """
        1. a) Add a scalar to a vector
        :param scalar:
        :type scalar: float
        :return: list
        """

        for i in range(len(self.__values)):
            self.__values[i] += scalar

        return self.__values[:]

    def addScalarToAVectorNp(self, scalar):
        """
        1. a) Add a scalar to a vector
        :param scalar:
        :type scalar: float
        :return: list
        """
        ##convert to numpy array
        self.__values = np.array(self.__values)

        ##adds scalar
        self.__values += scalar

        ##convert to a list
        self.__values = self.__values.tolist()

        return self.__values


    def addTwoVectors(self, other):
        """
        2. a) Add two vectors
        :param other:
        :type other: list
        :return: list
        """
        if isinstance(other, MyVector):
            if len(self.__values) == 0:
                return None
            else:
                if len(self.__values) == len(other.__values):
                    for i in range(len(self.__values)):
                        self.__values[i] = self.__values[i] + other.__values[i]
                    return self.values[:]
                else:
                    raise ValueError("The two vectors have different lengths")
        else:
            raise TypeError("The second vector is invalid")

    def addTwoVectorsNp(self, other):
        """
        2. a) Add two vectors using numpy
        :param other:
        :type other: list
        :return: list
        """
        if isinstance(other, MyVector):
            if len(self.__values) == 0:
                return None
            else:
                if len(self.__values) == len(other.__values):
                    arr1 = np.array(self.__values)
                    arr2 = np.array(other.__values)
                    sum = arr1 + arr2
                    sum = sum.tolist()
                    return sum
                else:
                    raise ValueError("The two vectors have different lengths")
        else:
            raise TypeError("The second vector is invalid")

    def subtractTwoVectors(self, other):
        """
        2. b) Subtract two vectors
        :param other:
        :type other: list
        :return: list
        """
        if isinstance(other, MyVector):
            if len(self.__values) == 0:
                return None
            else:

                if len(self.__values) == len(other.__values):
                    for i in range(len(self.__values)):
                        self.__values[i] = self.__values[i] - other.__values[i]
                    return self.values
                else:
                    raise ValueError("The two vectors have different lengths")
        else:
            raise TypeError("The second vector is invalid")

    def subrtactTwoVectorsNp(self, other):
        """
        2. b) Subtract two vectors using numpy
        :param other:
        :type other: list
        :return
        """
        if isinstance(other, MyVector):
            if len(self.__values) == 0:
                return None
            else:
                if len(self.__values) == len(other.__values):
                    arr1 = np.array(self.__values)
                    arr2 = np.array(other.__values)
                    dif = arr1 - arr2
                    dif = dif.tolist()
                    return dif
                else:
                    raise ValueError("The two vectors have different lengths")
        else:
            raise TypeError("The second vector is invalid")


    def multiplyTwoVectors(self, other):
        """
        2. c) Multiplication of 2 vectors
        :param other:
        :type other: list
        :return: float
        """
        if isinstance(other, MyVector):
            if len(self.__values) == 0:
                return None
            else:
                if len(self.__values) == len(other.__values):
                    k = 0
                    for i in range(len(self.__values)):
                        self.__values[i] = self.__values[i] * other.__values[i]
                        k = k + self.__values[i]
                    return k
                else:
                    raise ValueError("The two vectors have different lengths")
        else:
            raise TypeError("The second vector is invalid")

    def multiplyTwoVectorsNp(self, other):
        """
        2. c) Multiplication of 2 vectors using numpy
        :param other:
        :type other: list
        :return: float
        """
        if isinstance(other, MyVector):
            if len(self.__values) == 0:
                return None
            else:
                if len(self.__values) == len(other.__values):
                    arr1 = np.array(self.__values)
                    arr2 = np.array(other.__values)
                    product = arr1 * arr2
                    return np.sum(product)
                else:
                    raise ValueError("The two vectors have different lengths")
        else:
            raise TypeError("The second vector is invalid")

    def sumOfElements(self):
        """
        3. a) Sum of elements in a vector
        :return: float
        """

        if len(self.__values) == 0:
            return None
        else:
            k = 0
            for element in self.__values:
                k = k + element
            return k

    def sumOfElementsNp(self):
        """
        3. a) Sum of elements in a vector using numpy
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            arr = np.array(self.__values)
            return np.sum(arr)

    def productOfElements(self):
        """
        3. b) Product of elements in a vector
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            k = 1
            for element in self.__values:
                k = k * element
            return k

    def productOfElementsNp(self):
        """
        3. b) Product of elements in a vector using numpy
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            arr = np.array(self.__values)
            return np.prod(arr)

    def averageOfElements(self):
        """
        3. c) Average of elements in a vector
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            sum = 0
            for element in self.__values:
                sum = sum + element
            numberElements = len(self.__values)
            return sum/numberElements

    def averageOfElementsNp(self):
        """
        3. c) Average of elements in a vector using numpy
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            arr = np.array(self.__values)
            return np.mean(arr)

    def minimumOfVector(self):
        """
        3. d) Minimum of a vector
        :return: float
        """

        if len(self.__values) == 0:
            return None
        else:
            min = self.__values[0]
            for element in self.__values:
                if element < min:
                    min = element
            return min

    def minimumOfVectorNp(self):
        """
        3. d) Minimum of a vector using numpy
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            arr = np.array(self.__values)
            return np.min(arr)

    def maximumOfVector(self):
        """
        3. e) Maximum of a vector
        :return: float
        """

        if len(self.__values) == 0:
            return None
        else:
            max = self.__values[0]
            for element in self.__values:
                if element > max:
                    max = element
            return max

    def maximumOfVectorNp(self):
        """
        3. e) Maximum of a vector using numpy
        :return: float
        """
        if len(self.__values) == 0:
            return None
        else:
            arr = np.array(self.__values)
            return np.max(arr)


class VectorRepository():
    __markerPreset = ['o', 's', '^', 'D']
    def __init__(self, initialVectors = None):
        """
            Creating a repository containing vectors
        """

        self.__list_of_vectors = []
        if initialVectors is not None:
            # check if the nameIds are unique
            for vector in initialVectors:
                if isinstance(vector, MyVector):
                    self.__list_of_vectors.append(vector)

    def __repr__(self):
        """
        Return the string representation of the class.
        :return:
        :rtype: str
        """
        if len(self.__list_of_vectors) == 0:
            return "No vectors!"
        else:
            str_repr = ""
            for vector in self.__list_of_vectors:
                str_repr += str(vector) + "\n"
            return str_repr

    def __eq__(self, other):
        if self.getVectorCount() != other.getVectortCount():
            return False
        else:
            index = 0
            while index < self.getVectorCount():
                if self.__list_of_vectors[index] != other.__list_of_vectors[index]:
                    return False
                index += 1
            return True

    def getVectorCount(self):

        return len(self.__list_of_vectors)

    def addVector(self, nameId, colour, typeVector, values):
        """
        ex1:
        Add a new vector to the repository
        :param nameId:
        :type nameId: int, str
        :param colour:
        :type colour: str
        :param typeVector:
        :type typeVector: int
        :param values:
        :type values: list
        :return:
        :rtype:
        """
        if hC.checkColour(colour) == 1 and hT.checkType(typeVector) == 1:
            self.__list_of_vectors.append(MyVector(nameId, colour, typeVector, values))
        else:
            if hC.checkColour(colour) == 0 and hT.checkType(typeVector) == 1:
                raise ValueError("Vector not added. The accepted colors are: ‘red’, ‘green’, ‘blue’, ‘yellow’ and ‘magenta’")
            if hC.checkColour(colour) == 1 and hT.checkType(typeVector) == 0:
                raise ValueError("Vector not added. The type has to be a positive integer greater or equal to 0")
            if hC.checkColour(colour) == 0 and hT.checkType(typeVector) == 0:
                raise ValueError("Vector not added. The accepted colors are: ‘red’, ‘green’, ‘blue’, ‘yellow’ and ‘magenta’. The type has to be a positive integer greater or equal to 0")

    def getVectors(self):
        """
        ex2:
        Get all vectors from the repository
        :return:
        :rtype: list
        """

        return self.__list_of_vectors[:]

    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of vectors
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__list_of_vectors) or 0 == index == len(self.__list_of_vectors)

    def getVectorAtGivenIndex(self, index):
        """
        ex3:
        Get a vector at a given index
        :param index:
        :type index: int
        :return:
        :rtype: MyVector
        """

        if self.__isIndexCorrect(index):
            return self.__list_of_vectors[index]
        else:
            raise IndexError("Index invalid")

    def __getitem__(self, index):
        return self.getVectorAtGivenIndex(index)

    def updateVectorAtGivenIndex(self, index, nameId, colour, typeVector, values):
        """
        ex4:
        Update a vector at a given index
        :param index:
        type index: int
        :param nameId:
        :type nameId: int, str
        :param colour:
        :type colour: str
        :param typeVector:
        :type typeVector: int
        :param values:
        :type values: list
        :return:
        :rtype: MyVector
        """
        ok = 1
        for elem in self.__list_of_vectors:
            if elem.nameId == nameId:
                ok = 0
                break

        if self.__isIndexCorrect(index):
            if ok == 1:
                vector = self.__list_of_vectors[index]
                vector.nameId = nameId
                vector.colour = colour
                vector.typeVector = typeVector
                vector.values = values
            else:
                raise ValueError("The nameId is already in the list")
        else:
            raise IndexError("Index invalid")

    def updateVectorByNameId(self, atNameId, nameId, colour, typeVector, values):
        """
        ex5:
        Update a vector identified by nameId
        :param atNameId:
        type atNameId: int, str
        :param nameId:
        :type nameId: int, str
        :param colour:
        :type colour: str
        :param typeVector:
        :type typeVector: int
        :param values:
        :type values: list
        :return:
        :rtype: MyVector
        """

        i = 0
        while self.__list_of_vectors[i].nameId != atNameId and i < len(self.__list_of_vectors):
            i = i + 1


        if i < len(self.__list_of_vectors):
            vector = self.__list_of_vectors[i]
            vector.nameId = nameId
            vector.colour = colour
            vector.typeVector = typeVector
            vector.values = values
        else:
            raise ValueError("Doesn't exist")


    def deleteVectorByIndex(self, index):
        """
        ex6: Delete vector by index
        :param index:
        :type index: int
        :return:
        :rtype: MyVector
        """

        if self.__isIndexCorrect(index):
            del self.__list_of_vectors[index]
        else:
            raise IndexError("Index is not correct")

    def deleteVectorByNameId(self, nameId):
        """
        ex7: Delete vector by nameId
        :param nameId:
        :type nameId: int
        :return:
        :rtype: MyVector
        """

        index = len(self.__list_of_vectors) - 1
        while index >= 0:
            vector = self.__list_of_vectors[index]
            if vector.nameId == nameId:
                del self.__list_of_vectors[index]
            index -= 1

    def plotAllVectors(self):
        for vector in self.__list_of_vectors:
            if vector.typeVector > 3:
                type1 = 4
            else:
                type1 = vector.typeVector
            plt.plot(np.linspace(0, len(vector.values) - 1, len(vector.values)), vector.values, vector.colour + self.__markerPreset[type1 - 1])
        plt.show()
        plt.close()

if __name__ == "__main__":
    repo = VectorRepository([MyVector(1, 'y', 1, [1, 4, 9, 16, 25]), MyVector(2, 'g', 3, [3,2,1])])
    print(repo.getVectorAtGivenIndex(1))



















