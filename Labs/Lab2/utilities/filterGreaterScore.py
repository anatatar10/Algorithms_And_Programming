def filterGreaterScore(score_list, value): # the function keeps only participants whose scores are higher than the given value, removing the others
    new_score_list = [] ## empty list to store the participants
    for i in score_list: ## the function goes through the list
        if i > value: ## the function checks if the score is higher than the given value
            new_score_list.append(i) ## if the score respects the condition, it is added to the empty list
    return new_score_list ## the function return the new list with participants

"""score_list = [1,2,3,4,5,6,7,8,9,10]
print(filterGreaterScore(score_list, 12))
print(filterGreaterScore(score_list, 0))
print(filterGreaterScore(score_list, 10))
print(filterGreaterScore(score_list, 9))
print(filterGreaterScore(score_list, 2))
print(filterGreaterScore(score_list, 1))
print(filterGreaterScore(score_list, 5))
print(filterGreaterScore(score_list, 7))
print(filterGreaterScore(score_list, 4))
print(filterGreaterScore(score_list, 6))"""