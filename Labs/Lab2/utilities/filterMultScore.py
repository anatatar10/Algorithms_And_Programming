def filterMultScore(score_list, value): ## the function keeps only participants whose scores are multiple of the given value, removing the others
    new_score_list = [] ## the empty list where the participants are stored
    for i in score_list: ## the function goes through the list
        if i % value == 0: ## the function checks if the score is multiple of the given value
            new_score_list.append(i) ## if the score is multiple, it is added to the empty list
    return new_score_list ## the function returns the new list with participants

"""score_list = [1,2,3,4,5,6,7,8,9,10]

print(filterMultScore(score_list, 2))
print(filterMultScore(score_list, 10))
print(filterMultScore(score_list, 1))
print(filterMultScore(score_list, 3))
print(filterMultScore(score_list, 4))
print(filterMultScore(score_list, 5))
print(filterMultScore(score_list, 6))
print(filterMultScore(score_list, 7))
print(filterMultScore(score_list, 8))
print(filterMultScore(score_list, 11))"""