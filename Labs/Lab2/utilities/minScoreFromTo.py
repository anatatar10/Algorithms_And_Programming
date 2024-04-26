def minScoreFromTo(score_list, index1, index2): ## the function gets the minimum score for participants between 2 given indexes
    if index1 < 0 or index1 >= len(score_list):
        raise ValueError("Value not valid!")
    if index2 < 0 or index2 >= len(score_list):
        raise ValueError("Value not valid!")
    minim = 11 ## variable initialised with a value greater than the maximum possible score, which is 10
    for i in range(index1, index2 + 1): ## the function goes through the list from the element on index 1 until the element on index 2
        if score_list[i] < minim: ## the function checks if the element is less than the current minimum found
            minim = score_list[i] ## if the element is less than the minimum, it becomes the new current minimum
    return minim ## the function return the minimum found between 2 given indexes

"""score_list = [1,2,3,4,5,6,7,8,9,10]

print(minScoreFromTo(score_list, 0, 9))
print(minScoreFromTo(score_list, 1, 9))
print(minScoreFromTo(score_list, 3, 9))
print(minScoreFromTo(score_list, 4, 9))
print(minScoreFromTo(score_list, 5, 7))
print(minScoreFromTo(score_list, 7, 9))
print(minScoreFromTo(score_list, 3, 6))
print(minScoreFromTo(score_list, 2, 5))
print(minScoreFromTo(score_list, 5, 8))
print(minScoreFromTo(score_list, 8, 9))"""

