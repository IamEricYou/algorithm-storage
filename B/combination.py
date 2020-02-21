import itertools
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

# 

'''
Ex)
4 2

1 1
1 2
1 3
1 4
2 2
2 3 
2 4
3 3
3 4
4 4

'''

#Get the result as tuple
result = itertools.combinations(range(1,first+1), second)

#print the result
for i in range(0, first+1):
    for x in result:
        print(x)