def avgScoreFromTo(score_list, index1, index2): ## the function calculates the average score for participants between 2 given indexes
    if index1 < 0 or index1 >= len(score_list):
        raise ValueError("Value not valid!")
    if index2 < 0 or index2 >= len(score_list):
        raise ValueError("Value not valid!")
    sum = 0 ## initialise the sum with 0
    number = index2 - index1 + 1 ## counting the number of elements between 2 given indexes
    for i in range(index1, index2 + 1): ## the function goes through the list from the element on index 1 until the element on index 2
        sum += score_list[i] ## the scores are sumed into the variable sum
    average = float(sum / number) ## formula for the average score
    return average ## the function return the average score

"""score_list = [1,2,3,4,5,6,7,8,9,10]

print(avgScoreFromTo(score_list, 0, 1))
print(avgScoreFromTo(score_list, 0, 9))
print(avgScoreFromTo(score_list, 1, 5))
print(avgScoreFromTo(score_list, 7, 9))
print(avgScoreFromTo(score_list, 2, 3))
print(avgScoreFromTo(score_list, 3, 5))
print(avgScoreFromTo(score_list, 5, 9))
print(avgScoreFromTo(score_list, 2, 6))
print(avgScoreFromTo(score_list, 3, 8))
print(avgScoreFromTo(score_list, 1, 4))"""

