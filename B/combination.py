# Calculated by using combination
def npr(n,r):
    result = 1
    while(r != 0):
        result = result * n
        n = n - 1
        r = r - 1
    return result

value = input()

values = value.split(" ")
first = int(values[0])
second = int(values[1])

print(npr(first,second))