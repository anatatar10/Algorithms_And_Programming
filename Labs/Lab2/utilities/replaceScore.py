def replaceScore(score_list, index, newValue): ## the function replaces the score on the given index with a new given value
    if index < 0 or index >= len(score_list):
        raise ValueError("Wrong index!")
    if newValue < 0 or newValue > 10:
        raise ValueError("Wrong value!")
    score_list[index] = newValue ## the element on the given index gets a new value from the user
    return score_list ## return the updated list

"""score_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(replaceScore(score_list, 9, 10))
print(replaceScore(score_list, 0, 1))
print(replaceScore(score_list, 5, 7))
print(replaceScore(score_list, 3, 9))
print(replaceScore(score_list, 2, 5))
print(replaceScore(score_list, 8, 3))
print(replaceScore(score_list, 3, 5))
print(replaceScore(score_list, 5, 3))
print(replaceScore(score_list, 2, 9))
print(replaceScore(score_list, 6, 4))"""
