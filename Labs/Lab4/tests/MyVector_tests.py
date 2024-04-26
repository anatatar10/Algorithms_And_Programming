from domain import MyVector as v
from unittest import TestCase

class MyVectorTestClass(TestCase):
    def setUp(self):
        self.vector1 = v.MyVector(1, 'y', 1, [1, 4, 9, 16, 25])
        self.vector2 = v.MyVector(3, 'r', 5, [1, 2, 3])
        self.vector3 = v.MyVector(3, 'm', 2, [1, 1, 1, 1, 1])

    def testCreateVector(self):
        self.assertEqual(self.vector1.nameId, 1)
        self.assertEqual(self.vector1.colour, 'y')
        self.assertEqual(self.vector1.typeVector, 1)
        self.assertEqual(self.vector1.values, [1, 4, 9, 16, 25])
        self.assertRaises(ValueError, v.MyVector, 1, 'w', 1, [-1])

    def testSetNameId(self):
        self.vector1.nameId = 2
        self.assertEqual(self.vector1.nameId, 2)

    def testSetColour(self):
        self.vector1.colour = 'r'
        self.assertEqual(self.vector1.colour, 'r')

    def testSetTypeVector(self):
        self.vector1.typeVector = 2
        self.assertEqual(self.vector1.typeVector, 2)

    def testSetValues(self):
        self.vector1.values = [1,2,3]
        self.assertEqual(self.vector1.values, [1,2,3])

    def testStringRepresentation(self):
        self.assertEqual(str(self.vector1), "[MyVector(1, 'y', 1, [1, 4, 9, 16, 25]]")

    def testAddScalarToVector(self):
       self.vector1.addScalarToAVector(3)
       self.assertEqual(self.vector1.values, [4, 7, 12, 19, 28])

    def testAddTwoVectors(self):
        self.vector1.addTwoVectors(self.vector3)
        self.assertEqual(self.vector1.values, [2, 5, 10, 17, 26])

    def testSubtractTwoVectors(self):
        self.vector1.subtractTwoVectors(self.vector3)
        self.assertEqual(self.vector1.values, [0, 3, 8, 15, 24])

    def testMultiplyTwoVectors(self):
        self.assertEqual(self.vector1.multiplyTwoVectors(self.vector3), 55)

    def testSumOfElements(self):
        self.assertEqual(self.vector1.sumOfElements(), 55)

    def testProductOfElements(self):
        self.assertEqual(self.vector1.productOfElements(), 14400)

    def testAverageOfElements(self):
        self.assertEqual(self.vector1.averageOfElements(), 11)

    def testMinimumOfVector(self):
        self.assertEqual(self.vector1.minimumOfVector(), 1)

    def testMaximumOfVector(self):
        self.assertEqual(self.vector1.maximumOfVector(), 25)

class VectorRepositoryTestClass(TestCase):
    def setUp(self):
        self.emptyRepository = v.VectorRepository([])
        self.repository1 = v.VectorRepository([v.MyVector(1, 'y', 1, [1, 4, 9, 16, 25]), v.MyVector(2, 'g', 3, [3,2,1])])
        self.repository2 = v.VectorRepository(
            [v.MyVector(1, 'b', 3, []), v.MyVector(5, 'r', 2, [5, 1, 3, 10]), v.MyVector(3, 'm', 1, [2.5, 7, 4])])

    def testCreateVectorRepository(self):
        self.assertEqual(self.emptyRepository.getVectorCount(), 0)
        self.assertEqual(self.repository1.getVectorCount(), 2)
        self.assertEqual(self.repository2.getVectorCount(), 3)

    def testAddVector(self):
        self.emptyRepository.addVector(1, 'b', 3, [11, 9])
        self.assertEqual(self.emptyRepository.getVectorCount(), 1)

    def testGetVectorAtGivenIndex(self):
        self.assertEqual(str(self.repository1.getVectorAtGivenIndex(0)), "MyVector(1, 'y', 1, [1, 4, 9, 16, 25])")

    def testUpdateVectorAtGivenIndex(self):
        self.repository1.updateVectorAtGivenIndex(0, 5, 'm', 2, [1, 4])
        self.assertEqual(str(self.repository1.getVectorAtGivenIndex(0)), "MyVector(5, 'm', 2, [1, 4])")

    def testUpdateVectorByNameId(self):
        self.repository1.updateVectorByNameId(1, 2, 'b', 2, [])
        self.assertEqual(str(self.repository1.getVectorAtGivenIndex(0)), "MyVector(2, 'b', 2, [])")

    def testDeleteVectorByIndex(self):
        self.repository1.deleteVectorByIndex(0)
        self.assertEqual(self.repository1.getVectorCount(), 1)

    def testDeleteVectorByNameId(self):
        self.repository1.deleteVectorByNameId(1)
        self.assertEqual(self.repository1.getVectorCount(), 1)


