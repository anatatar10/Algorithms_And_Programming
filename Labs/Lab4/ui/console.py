from domain import MyVector as v

def dataExamples():
    vector = v.MyVector(1, 'y', 1, [1,2,3])
    vector1 = v.MyVector(2, 'b', 3, [5, 8, 10])
    repo = v.VectorRepository([v.MyVector(1, 'b', 3, []), v.MyVector(5, 'r', 2, [5, 1, 3, 10]), v.MyVector(3, 'm', 1, [2.5, 7, 4]), v.MyVector(7, 'y', 4, [3, 9, 7, 2, 5])])
    print(vector)
    print("1.st iteration\n")

    print("ex 1 a):")
    print("Add 3 to the vector")
    vector.addScalarToAVector(3)
    print(vector)
    print("Add 1 to the vector")
    vector.addScalarToAVector(1)
    print(vector)
    print("Add -2 to the vector")
    vector.addScalarToAVector(-2)
    print(vector)
    try:
        print("Add -1 to the vector")
        vector.addScalarToAVector(-1)
    except ValueError as ve:
        print(ve)
    print(vector)
    print("Add 2.5 to the vector")
    vector.addScalarToAVector(2.5)
    print(vector)
    print("Add -3.5 to the vector")
    vector.addScalarToAVector(-3.5)
    print(vector)
    print("Add 10 to the vector")
    vector.addScalarToAVector(10)
    print(vector)
    print("Add -2 to the vector")
    vector.addScalarToAVector(-2)
    print(vector)
    print("Add 3 to the vector")
    vector.addScalarToAVector(3)
    print(vector)
    print("Add 1 to the vector")
    vector.addScalarToAVector(1)
    print(vector)
    print()
    print("ex 2 a):")
    print("Add vector (2, 'b', 3, [5, 8, 10]) to the vector")
    vector.addTwoVectors(vector1)
    print(vector)
    print("ex 2 b):")
    print("Subtract vector (2, 'b', 3, [5, 8, 10]) from the vector")
    vector.subtractTwoVectors(vector1)
    print(vector)
    print("ex 2 c):")
    print("Multiply the vector with vector (2, 'b', 3, [5, 8, 10])")
    vector.multiplyTwoVectors(vector1)
    print(vector)
    print()

    print(vector)
    print("ex 3 a):")
    print("The sum of the elements of vector is:")
    print(vector.sumOfElements())
    print("ex 3 b):")
    print("The product of the elements of vector is:")
    print(vector.productOfElements())
    print("ex 3 c):")
    print("The average of the elements of vector is:")
    print(vector.averageOfElements())
    print("ex 3 d):")
    print("The minimum of the vector is:")
    print(vector.minimumOfVector())
    print("ex 3 e):")
    print("The maximum of the vector is:")
    print(vector.maximumOfVector())
    print()
    print(repo)
    print("2nd iteration")
    print()
    print("ex 1:")
    print("Add vector (2, 'b', 3, [5, 8, 10]) to the repository")
    repo.addVector(2, 'b', 3, [5, 8, 10])
    print(repo)
    print("Add vector (4, 'm', 2, [-1, 2.5, 10]) to the repository")
    repo.addVector(4, 'm', 2, [-1, 2.5, 10])
    print(repo)
    try:
        repo.addVector(6, 'w', 1, [])
    except ValueError as ve:
        print(ve)
    print(repo)
    try:
        repo.addVector(6, 'b', -2, [])
    except ValueError as ve:
        print(ve)
    print(repo)
    try:
        repo.addVector(6, 'w', -2.5, [])
    except ValueError as ve:
        print(ve)
    print(repo)
    try:
        repo.addVector(6, 'b', 3, [])
    except ValueError as ve:
        print(ve)
    print(repo)
    print("Add vector (8, 'b', 3, [-5, 8]) to the repository")
    repo.addVector(8, 'b', 3, [5, 8])
    print(repo)
    print("Add vector (9, 'm', 1 [-1]) to the repository")
    repo.addVector(9, 'm', 1, [-1])
    print(repo)
    print()
    print("ex 2: Get all vectors")
    print(repo.getVectors())
    print()
    print(repo)
    print("ex 3:")
    print("Get vector at index 0")
    print(repo.getVectorAtGivenIndex(0))
    print("Get vector at index 1")
    print(repo.getVectorAtGivenIndex(1))
    print("Get vector at index 2")
    print(repo.getVectorAtGivenIndex(2))
    print("Get vector at index 3")
    print(repo.getVectorAtGivenIndex(3))
    print("Get vector at index 4")
    print(repo.getVectorAtGivenIndex(4))
    print("Get vector at index -2")
    try:
        repo.getVectorAtGivenIndex(-2)
    except IndexError as ie:
        print(ie)
    print("Get vector at index 5")
    try:
        print(repo.getVectorAtGivenIndex(5))
    except IndexError as ie:
        print(ie)
    print("Get vector at index 6")
    print(repo.getVectorAtGivenIndex(6))
    print("Get vector at index 7")
    print(repo.getVectorAtGivenIndex(7))
    print()
    print(repo)
    print("ex 4:")
    print("Update vector at index 4")
    repo.updateVectorAtGivenIndex(4, 12, 'm', 2, [11])
    print(repo)
    print()
    print(repo)
    print("ex 5:")
    print("Update vector with nameid = 1 with (11, 'y', 3, [1,2])")
    repo.updateVectorByNameId(1, 11, 'y', 3, [1,2])
    print(repo)
    print("Update vector with nameid = 5")
    repo.updateVectorByNameId(5, 99, 'b', 1, [1, 99])
    print(repo)
    try:
        repo.updateVectorByNameId(9, 9, 'y', 1, [])
    except ValueError as ve:
        print(ve)
    print("Update vector with nameid = 7 with (23, 'y', 2, [5, 32])")
    repo.updateVectorByNameId(7, 23, 'y', 2, [5, 32])
    print(repo)
    print()
    print(repo)
    print("ex 6:")
    print("Delete vector at index 0")
    repo.deleteVectorByIndex(0)
    print(repo)
    print("Delete vector at index 1")
    repo.deleteVectorByIndex(1)
    print(repo)
    print("Delete vector at index 2")
    repo.deleteVectorByIndex(2)
    print(repo)
    try:
        print("Delete vector at index -2")
        print(repo.deleteVectorByIndex(-2))
    except IndexError as ie:
        print(ie)
    try:
        print("Delete vector at index 10")
        print(repo.deleteVectorByIndex(10))
    except IndexError as ie:
        print(ie)
    try:
        print("Delete vector at index -5")
        print(repo.deleteVectorByIndex(-5))
    except IndexError as ie:
        print(ie)
    try:
        print("Delete vector at index 12")
        print(repo.deleteVectorByIndex(12))
    except IndexError as ie:
        print(ie)
    print()
    print(repo)
    print("ex 7: ")
    print("Delete vector with nameid = 99")
    repo.deleteVectorByNameId(99)
    print(repo)
    repo.deleteVectorByNameId(4)
    print(repo)
    try:
        print("Delete vector with nameid = 12")
        print(repo.deleteVectorByNameId(12))
    except ValueError as ve:
        print(ve)
    print(repo)
    try:
        print("Delete vector with nameid = -1")
        print(repo.deleteVectorByNameId(-1))
    except ValueError as ve:
        print(ve)
    print(repo)
    repo.plotAllVectors()

def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - Add a vector to the repository")
    print(" 2 - Get all vectors")
    print(" 3 - Get a vector at a given index")
    print(" 4 - Update a vector at a given index ")
    print(" 5 - Update a vector identified by nameid")
    print(" 6 - Delete a vector by index")
    print(" 7 - Delete a vector by nameid")
    print(" 8 - Plot all the vectors")

def start():
    print()
    vec_repo = v.VectorRepository()
    printMenu()
    command = None
    while command != 0:  # while True
        try:    # catches all conversion errors
            command = int(input(">>> "))
            if command == -2:
                dataExamples()
            elif command == -1:
                printMenu()
            elif command == 0:
                print("program ended")
            elif command == 1:
                nameId = int(input("nameId of the vector: "))
                colour = input("Color of the vector: ")
                typeVector = int(input("Type of the vector: "))
                values = []
                n = int(input("Enter number of elements in the values: "))
                for i in range(0, n):
                    ele = int(input())
                    values.append(ele)
                try:
                    vec_repo.addVector(nameId, colour, typeVector, values)
                    print(vec_repo)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                print(vec_repo.getVectors())
            elif command == 3:
                index = int(input("Index: "))
                try:
                    vec_repo.getVectorAtGivenIndex(index)
                    print(vec_repo)
                except IndexError as ie:
                    print(ie)
            elif command == 4:
                index = int(input("index: "))
                nameId = int(input("nameId of the vector: "))
                colour = input("Color of the vector: ")
                typeVector = int(input("Type of the vector: "))
                values = []
                n = int(input("Enter number of elements in the values: "))
                for i in range(0, n):
                    ele = int(input())
                    values.append(ele)
                try:
                    vec_repo.updateVectorAtGivenIndex(index, nameId, colour, typeVector, values)
                    print(vec_repo)
                except IndexError as ie:
                    print(ie)
            elif command == 5:
                atNameId = int(input("NameId at which the vector is modified: "))
                nameId = int(input("nameId of the vector: "))
                colour = input("Color of the vector: ")
                typeVector = int(input("Type of the vector: "))
                values = []
                n = int(input("Enter number of elements in the values: "))
                for i in range(0, n):
                    ele = int(input())
                    values.append(ele)
                try:
                    vec_repo.updateVectorByNameId(atNameId, nameId, colour, typeVector, values)
                    print(vec_repo)
                except ValueError as ve:
                    print(ve)
            elif command == 6:
                index = int(input("Index: "))
                try:
                    vec_repo.deleteVectorByIndex(index)
                    print(vec_repo)
                except IndexError as ie:
                    print(ie)
            elif command == 7:
                nameId = int(input("NameId: "))
                try:
                    vec_repo.deleteVectorByNameId(nameId)
                    print(vec_repo)
                except ValueError as ve:
                    print(ve)
            elif command == 8:
                vec_repo.plotAllVectors()
            else:
                print("invalid command")
        except ValueError:
            print("invalid type entered")



