def lessScore(score_list, value): ## the function gets the participants with the score less then the given value
    if value < 0 or value > 10:
        raise ValueError("Value not valid!")
    listParticipants = [] ## creating an empty list to store the participants
    for i in range(0, len(score_list)): ## the function goes trough the list and checks the condition for each participant
        if score_list[i] < value: ## the function checks if the score is less than the given value
            listParticipants.append(i) ## when a score less than the value is found, the participant's position is stored in the empty list
    return listParticipants ## the function returns the updated list

"""score_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(lessScore(score_list, 1))
print(lessScore(score_list, 2))
print(lessScore(score_list, 3))
print(lessScore(score_list, 4))
print(lessScore(score_list, 5))
print(lessScore(score_list, 6))
print(lessScore(score_list, 7))
print(lessScore(score_list, 8))
print(lessScore(score_list, 9))
print(lessScore(score_list, 10))"""


