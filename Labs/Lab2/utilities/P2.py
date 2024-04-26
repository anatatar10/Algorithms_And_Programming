
##ex1
def addScore(value, score_list):
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    score_list.append(value)
    return score_list

def insertScore(value, index, score_list):
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    if index < 0 or index > len(score_list):
        raise ValueError("Index out of range")
    score_list.insert(index, value)
    return score_list


##ex2:
def removeScore(index, score_list):
    if index < 0 or index > len(score_list) - 1:
        raise ValueError("Index out of range")
    for i in range(index, len(score_list) - 1):
        score_list[i] = score_list[i+1]
    score_list.pop()
    return score_list

def removeScoreFromTo(from_index, to_index, score_list):
    if to_index < from_index or to_index >= len(score_list) or from_index < 0:
        raise ValueError("Index is not valid")
    for i in range(from_index, to_index+1):
        del score_list[i]
    return score_list

def replaceScore(newValue, index, score_list):
    if newValue < 0 or newValue > 10:
        raise ValueError("Score must be between 0 and 10")
    if index < 0 or index >= len(score_list):
        raise ValueError("Index out of range")
    score_list[index] = newValue
    return score_list


##ex3:
def lessScore(value, score_list):
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    listParticipants = []
    for i in range(0, len(score_list)):
        if score_list[i] < value:
            listParticipants.append(i)
    return listParticipants

def sortedScoreList(score_list):
    for i in range(0, len(score_list)):
        for j in range(i+1, len(score_list)):
            if(score_list[i] > score_list[j]):
                aux = score_list
                score_list[i] = score_list[j]
                score_list[i] = aux
    return score_list

def sortedScoreListHigher(score_list, value):
    listParticipantsHigher = []
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    for i in range(0, len(score_list)):
        if int(score_list[i]) > value:
            listParticipantsHigher.append(i)
    for i in range(0, len(listParticipantsHigher)):
        for j in range(i+1, len(listParticipantsHigher)):
            if(listParticipantsHigher[i] > listParticipantsHigher[j]):
                aux = listParticipantsHigher
                listParticipantsHigher[i] = listParticipantsHigher[j]
                listParticipantsHigher[i] = aux
    return listParticipantsHigher

##ex4:
def avgScoreFromTo(from_index, to_index, score_list):
    if to_index < from_index or to_index >= len(score_list) or from_index < 0:
        raise ValueError("the index is not valid")
    sum = 0
    number = to_index - from_index + 1
    for i in range(from_index, to_index+1):
        sum += score_list[i]
    average = float(sum / number)
    return average

def minScoreFromTo(from_index, to_index, score_list):
    if to_index < from_index or to_index >= len(score_list) or from_index < 0:
        raise ValueError("the index is not valid")
    min = 1000
    for i in range(from_index, to_index+1):
        if score_list[i] < min:
            min = score_list[i]
    return min

def multScoreFromTo(score_list, value, from_index, to_index):
    listParticipantsMult = []
    if to_index < from_index or to_index >= len(score_list) or from_index < 0:
        raise ValueError("Index is not valid")
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    for i in range(from_index, to_index + 1):
        if score_list[i] % value == 0:
            listParticipantsMult.append(score_list[i])
    return listParticipantsMult


##ex5:
def filterMultScore(score_list, value):
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    new_score_list = []
    for i in score_list:
        if i % value == 0:
            new_score_list.append(i)
    return new_score_list

def filterGreaterScore(score_list, value):
    if value < 0 or value > 10:
        raise ValueError("Score must be between 0 and 10")
    new_score_list = []
    for i in score_list:
        if i > value:
            new_score_list.append(i)
    return score_list

##ex6:
def undo(old_score_list, current_score_list, case):
    if case == 1 or case == 2 or case == 5:
        current_score_list = old_score_list
    return current_score_list

