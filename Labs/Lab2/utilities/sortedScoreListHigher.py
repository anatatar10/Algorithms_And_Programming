def sortedScoreListHigher(score_list, value): ## the function sortes the participants with scores higher than the given value
    if value < 0 or value > 10:
        raise ValueError("Value not valid!")
    listParticipantsHigher = [] ## empty list to store the sorted participants with scores higher than the given value
    for i in range(0, len(score_list)): ## the function goes through the list
        if int(score_list[i]) > value: ## the function checks if the element is greater than the given value
            listParticipantsHigher.append(i) ## if the elements is higher, the index of the participant is added to the list
    for i in range(0, len(listParticipantsHigher)): ## the function goes through the list until the last but one element
        for j in range(i+1, len(listParticipantsHigher)): ## the function goes through the list from the i+1 index until the last element
            if(listParticipantsHigher[i] > listParticipantsHigher[j]): ## the function compares two consecutive elements and checks if the first is greater than the second one
                aux = listParticipantsHigher ## the first element is saved as an auxiliar variablle
                listParticipantsHigher[i] = listParticipantsHigher[j] ## the first element gets the value of the second one
                listParticipantsHigher[i] = aux ## the second elements gets the value of the first one saved as the auxiliar variable
    return listParticipantsHigher ## the function returns the new list

"""print(sortedScoreListHigher([10,9,8,7,6,5,4,3,2,1], 3))
print(sortedScoreListHigher([10,9,8,7,6,5,4,3,2,1], 2))
print(sortedScoreListHigher([10,9,8,7,6,5,4,3,2,1], 5))
print(sortedScoreListHigher([9,8,7], 10))
print(sortedScoreListHigher([9,8,7, 1], 8))
print(sortedScoreListHigher([9,8,7,1], 2))
print(sortedScoreListHigher([10,9,8,7,6,5,4,3,2,1], 3))
print(sortedScoreListHigher([,6,5,4,3,2,1], 5))"""