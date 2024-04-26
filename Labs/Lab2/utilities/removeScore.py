def removeScore(score_list, index): ## the function removes an element at a given index
    if index < 0 or index >= len(score_list):
        raise ValueError("Index not valid!")
    for i in range(index, len(score_list) - 1): ## the function goes through the list starting from index to the end of the list
        score_list[i] = score_list[i+1] ## the function moves the elements from the index one position to the left
    score_list.pop() ## the function deletes the last element which is a duplicate
    return score_list ## returns the updated list

"""score_list = [1,2,3,4,5,6,7,8,9,10]

print(removeScore(score_list, 9))
print(removeScore(score_list, 8))
print(removeScore(score_list, 7))
print(removeScore(score_list, 6))
print(removeScore(score_list, 5))
print(removeScore(score_list, 4))
print(removeScore(score_list, 3))
print(removeScore(score_list, 2))
print(removeScore(score_list, 1))
print(removeScore(score_list, 0))"""


