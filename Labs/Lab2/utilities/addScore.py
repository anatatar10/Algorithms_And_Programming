def addScore(score_list, value): ## the function adds a value at the end of the list
    if value < 0 or value > 10:
        raise ValueError("Value not valid!")
    score_list.append(value) ## append the value to the end of the list
    return score_list ## return the updated list

"""score_list = []

print(addScore(score_list, 10))
print(addScore(score_list, 9))
print(addScore(score_list, 8))
print(addScore(score_list, 7))
print(addScore(score_list, 6))
print(addScore(score_list, 5))
print(addScore(score_list, 4))
print(addScore(score_list, 3))
print(addScore(score_list, 2))
print(addScore(score_list, 1))"""
