def removeScoreFromTo(score_list, index1, index2): ## the function removes elements between two given indexes
    if index1 < 0 or index1 >= len(score_list):
        raise ValueError("Wrong index!")
    if index2 < 0 or index2 >= len(score_list):
        raise ValueError("Wrong index!")
        index2 = readIndex()
    del score_list[index1:index2 + 1] ## the function deletes the elements starting from index 1 until index 2 + 1
    return score_list ## return the updated list


"""print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 2))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1, 8))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5, 6))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1, 3))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2, 7))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 8, 9))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2, 4))
print(removeScoreFromTo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4, 7))"""


