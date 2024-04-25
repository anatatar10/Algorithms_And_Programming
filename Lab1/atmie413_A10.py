"""Read integers numbers until number 0 is read. Print the number of pairs 𝒏𝟏 and 𝒏𝟐 of numbers read consecutively
with the property that the number of digits 5 from 𝒏1 is strictly higher than the number of digits 5 from 𝒏𝟐."""

def function(n):
    n = str(n)
    return n.count("5")

n1 = int(input("n = "))
if n1 != 0:
    ok = 1
    countNumbers = 0
    while ok == 1:
        n2 = int(input("n = "))
        if(n2 == 0):
            ok = 0
            break
        elif (function(n1) > function(n2)):
            countNumbers += 1
        n1 = n2
print(countNumbers)

