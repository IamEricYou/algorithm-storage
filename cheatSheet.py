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

'''
Iterable objects
'''

def li(item):
    x = 1 
    while True:
        yield item * x
        x += 1

ot = li(2)
print(ot)
print(next(ot))
print(next(ot))

li = iter([1,2,3])
print(next(li)) #1
print(next(li)) #2
print(next(li)) #3
print(next(li)) #StopIteration

'''
List operation
'''

# 문자열 뒤집기
a = 'abc'
print(a[::-1]) # 출력: cba

# 리스트 복사
a = [1, 2, 3]
b = a[:]
print(b)      # 출력: [1, 2, 3]
print(a is b) # 출력: False

c = [[1, 2], [3, 4]]
d = c[:]
c[0] = [5, 6] # 리스트 자체는 복사되지만
c[1][0] = 7   # 리스트의 원소들까지 복사되지는 않으므로 주의해서 사용하자.
print(c)      # 출력: [[5, 6], [7, 4]]
print(d)      # 출력: [[1, 2], [7, 4]]
print('%s, %s, %s' % (c is d, c[0] is d[0], c[1] is d[1])) # 출력: False, False, True