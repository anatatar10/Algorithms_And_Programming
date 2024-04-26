from UI.messageToTheUser import Message
from UI.read_case import readCase
from UI.read_index import readIndex
from UI.read_value import readValue
from utilities.addScore import addScore
from utilities.avgScoreFromTo import avgScoreFromTo
from utilities.filterMultScore import filterMultScore
from utilities.filterGreaterScore import filterGreaterScore
from utilities.insertScore import insertScore
from utilities.lessScore import lessScore
from utilities.minScoreFromTo import minScoreFromTo
from utilities.multScoreFromTo import multScoreFromTo
from utilities.removeScore import removeScore
from utilities.removeScoreFromTo import removeScoreFromTo
from utilities.replaceScore import replaceScore
from utilities.sortedScoreList import sortedScoreList
from utilities.sortedScoreListHigher import sortedScoreListHigher
from utilities.undo import undo
from utilities.print_array import printArray

print(Message()) ##prints the menu from which the user can select the next operation
case = readCase()
while case < 0 or case > 7:
    print("Wrong value! The case value needs to be between 0 and 7.")
    case = readCase()
score_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
prev_case = 0
prev_score_list = []
while case != 0:
    if case == 1:
        prev_score_list = score_list.copy()
        print("You have chosen to add a score in the list.\nIf you want to add it at the end of the list insert 1 and the value.\n"
              "Else insert 2, the index and the value.")
        sub_case = readCase() ##reads the next operation the user wants
        if sub_case == 1:
            value = readValue() ##reads the next value the user wants to add
            try:
                score_list = addScore(score_list, value)
            except ValueError as e:
                print(e)
        elif sub_case == 2:
            index = readIndex() ##reads the index that the user wants
            value = readValue()
            try:
                score_list = insertScore(score_list, index, value)
            except ValueError as e:
                print(e)
    elif case == 2:
        prev_score_list = score_list.copy()
        print("You have chosen to modify a score in the list. If you want to remove an element type 1 and the index.\nType 2, index 1 and index 2 to remove the elements between 2 indexes.\nType 3, the index and the new value to replace the score on the index with a new score")
        sub_case = readCase()
        if sub_case == 1:
            index = readIndex()
            try:
                score_list = removeScore(score_list, index)
            except ValueError as e:
                print(e)
        elif sub_case == 2:
            index1 = readIndex()
            index2 = readIndex()
            try:
                score_list = removeScoreFromTo(score_list, index1, index2)
            except ValueError as e:
                print(e)
        elif sub_case == 3:
            index = readIndex()
            value = readValue()
            try:
                score_list = replaceScore(score_list, index, value)
            except ValueError as e:
                print(e)
    elif case == 3:
        prev_score_list = score_list.copy()
        print("You have chosen to get the participants with scores having some properties.\nType 1 and the value to get participants with score less than the introduced value.\nType 2 to get all the participants sorted by their score.\nType 3 and the value to get the participants with scores higher than the introduced value.")
        sub_case = readCase()
        if sub_case == 1:
            value = readValue()
            try:
                score_list = lessScore(score_list, value)
            except ValueError as e:
                print(e)
        elif sub_case == 2:
            score_list = sortedScoreList(score_list)
        elif sub_case == 3:
            value = readValue()
            try:
                score_list = sortedScoreListHigher(score_list, value)
            except ValueError as e:
                print(e)
    elif case == 4:
        print("You have chosen to obtain different characteristics of participants.\nType 1, index 1 and index 2 to get the average score for participants between the given indexes.\n" 
              "Type 2, index 1 and index 2 to get the minimum score for participants between the two given indexes.\nType 3, index 1 and index 2 to get the score of participants between two given indexes, multiples of the introduced value")
        sub_case = readCase()
        if sub_case == 1:
            index1 = readIndex()
            index2 = readIndex()
            try:
                printArray(avgScoreFromTo(score_list, index1, index2))
            except ValueError as e:
                print(a)
        elif sub_case == 2:
            index1 = readIndex()
            index2 = readIndex()
            try:
                printArray(minScoreFromTo(score_list, index1, index2))
            except ValueError as e:
                print(e)
        elif sub_case == 3:
            value = readValue()
            index1 = readIndex()
            index2 = readIndex()
            try:
                printArray(multScoreFromTo(score_list, value, index1, index2))
            except ValueError as e:
                print(e)
    elif case == 5:
        prev_score_list = score_list.copy()
        print("You have chosen to filter the values in the list.\nType 1 and the value to keep only the participants with scores multiple of the value introduced, removing the others.\nType 2 and the value to keep only participants with scores higher than the introduced value, removing the others")
        sub_case = readCase()
        if sub_case == 1:
            value = readValue()
            score_list = filterMultScore(score_list, value)
        elif sub_case == 2:
            value = readValue()
            score_list = filterGreaterScore(score_list, value)
    elif case == 6:
        print("You have chosen to undo the last operation that modified the list")
        score_list = undo(prev_score_list, score_list)
    elif case == 7:
        print("The list is: ")
        printArray(score_list)
    case = readCase()
