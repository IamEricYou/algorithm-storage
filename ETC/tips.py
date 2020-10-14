def product(a, b):
    return a * b

def add(a, b):
    return a + b

i = True

value = (product if i else add)(5, 7)

print(value)

for ele in [1,2,3,4]:
    if ele > 4:
        print(ele)

    else:
        print("There is no 5")

li = [1,2,3,1,2,3,4]
print(list(set(li)))