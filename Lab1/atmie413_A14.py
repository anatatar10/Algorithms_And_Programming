"""Read a natural number 𝒏𝒏. Print the number of 1s from the binary representation of 𝒏𝒏."""

def bin(n):
    if(n < 2):
        return n
    else:
        return bin(n//2)+n%2

n = int(input("n= "))

print(bin(n))

