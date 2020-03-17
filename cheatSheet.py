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

'''
Conversions
'''

dict_exam = dict([(1,"Hi"), (2,"hello")])
print(dict_exam)
join_exam = ["hello","world"]
out_first = ''.join(join_exam)
out_second = ':'.join(join_exam)
print(out_first)
print(out_second)

a = [1,2,3,4]
b = {1,2,3,4}
c = {"1": 2, "3": 4}

#https://docs.python.org/3/tutorial/datastructures.html
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.count('tangerine')
fruits.append('grape')
fruits.sort()
fruits.pop() #Using list as stack
fruits.append(7) #List a push
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.popleft() # The second to arrive now leaves = Eric
queue                           