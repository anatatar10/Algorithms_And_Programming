def sortedScoreList(score_list): ## the function sorts all the participants by their score
    for i in range(0, len(score_list) - 1): ## the function goes through the list until the last but one element
        for j in range(i+1, len(score_list)): ## the function goes through the list from the i+1 index until the last element
            if score_list[i] > score_list[j]: ## the function compares two consecutive elements and checks if the first is greater than the second one
                aux = score_list[i] ## the first element is saved as an auxiliar variablle
                score_list[i] = score_list[j] ## the first element gets the value of the second one
                score_list[j] = aux ## the second elements gets the value of the first one saved as the auxiliar variable
    return score_list ## the function returns the updated list

"""print(sortedScoreList([10,9,8,7,6,5,4,3,2,1]))
print(sortedScoreList([3,7,1,8,4,5,7,2,9,10]))
print(sortedScoreList([6,4,2,10,1,8,3,9,5,7]))
print(sortedScoreList([1,2,3,4,5,6,7,8,9,10]))
print(sortedScoreList([3,6,2,9]))
print(sortedScoreList([3,2,1]))
print(sortedScoreList([8,3,5,6,1,9]))
print(sortedScoreList([10,2,4,7,1,6]))
print(sortedScoreList([9,8,7,6,5,4]))
print(sortedScoreList([3, 7, 5, 3, 2, 8]))


"""

