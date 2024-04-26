def insertScore(score_list, index, value): ## the function inserts the value at a given index
    if index < 0 or index >= len(score_list):
        raise ValueError("Index not valid!")
    if value < 0 or value > 10:
        raise ValueError("Value not valid!")
    score_list.insert(index, value) ## insert the value at index
    return score_list ##returns the updated list

"""score_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(insertScore(score_list, 3, 4))
print(insertScore(score_list, 5, 8))
print(insertScore(score_list, 1, 10))
print(insertScore(score_list, 7, 1))
print(insertScore(score_list, 2, 0))
print(insertScore(score_list, 0, 2))
print(insertScore(score_list, 8, 3))
print(insertScore(score_list, 6, 5))
print(insertScore(score_list, 10, 10))
print(insertScore(score_list, 4, 4))"""

