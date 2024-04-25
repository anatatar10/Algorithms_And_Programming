"""Print the number of common digits of two numbers, as well as the digits."""
def function(n, m):
    count = 0
    f = [0] * 10
    g = [0] * 10

    while(n != 0):
        f[n % 10] += 1
        n = n // 10
    while(m != 0):
        g[m % 10] += 1
        m = m // 10
    for i in range(10):
        if f[i] > 0 and g[i] > 0:
            count += 1
    print(count)
    for i in range(10):
        if f[i] > 0 and g[i] > 0:
            print(i, end = ", " )


n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
function(n, m)





