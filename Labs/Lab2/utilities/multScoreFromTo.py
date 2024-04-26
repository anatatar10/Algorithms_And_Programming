def multScoreFromTo(score_list, value, index1, index2): ## the function gets the score of the participants between 2 given indexes which are multiple of a given value
    if value < 0 or value > 10:
        raise ValueError("Wrong value!")
    while index1 < 0 or index1 >= len(score_list):
        raise ValueError("Wrong index!")
    while index2 < 0 or index2 >= len(score_list):
        raise ValueError("Wrong index!")
    listParticipantsMult = [] ## the empty list where the scores of the participants will be stored
    for i in range(index1, index2 + 1): ## the function goes through the list from the element on index 1 until the element on index 2
        if score_list[i] % value == 0: ## the function checks if the score is multiple of the given value
            listParticipantsMult.append(score_list[i]) ## if the score is multiple of the value, it is added to the empty list
    return listParticipantsMult ## the function returns a new list with the scores multiple of the given value

"""score_list = [1,2,3,4,5,6,7,8,9,10]

print(multScoreFromTo(score_list, 2, 0, 9))
print(multScoreFromTo(score_list, 4, 0, 9))
print(multScoreFromTo(score_list, 6, 0, 9))
print(multScoreFromTo(score_list, 3, 0, 9))
print(multScoreFromTo(score_list, 1, 0, 9))
print(multScoreFromTo(score_list, 5, 0, 9))
print(multScoreFromTo(score_list, 2, 0, 6))
print(multScoreFromTo(score_list, 7, 0, 9))
print(multScoreFromTo(score_list, 4, 0, 6))
print(multScoreFromTo(score_list, 3, 0, 5))"""