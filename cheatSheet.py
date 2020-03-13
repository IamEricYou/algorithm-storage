#!/user/bin/env python

# Basic list Operation

a = [1, 2, 3, 4, 5]
print(a[:-1])  # Print list without the last index
print(a[::-1])  # print backwards
print(a.index(3))  # print index where 3 is at
print(a[::2])  # print every 2 indexes
del a[::2]  # delete item by coresponding indexes
div, mod = divmod(5, 2)  # Return quotient and remainder
print(div, mod)
# method adds counter to an iterable and returns it (the enumerate object).
exam_first = enumerate(a, start=12)

print(list(exam_first))


'''
Lambda in Python
'''

b = [1, 2, 3, 4, 5]


def x(a): return a + a
x_l = lambda a : a + a

lambda_exam = map(x_l, b)
print(set(lambda_exam))

colors = ["Goldenrod", "purple", "Salmon", "turquoise", "cyan"]
print(sorted(colors, key=lambda s: s.casefold()))
print("Hello".casefold())

'''
Lambda can be problematic, just use def!
'''

def case_ignore(str): return str.casefold()
print(sorted(colors, key=case_ignore))