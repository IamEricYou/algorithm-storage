#!/user/bin/env python

# Basic list Operation

a = [1, 2, 3, 4, 5]
# print(a[:-1])  # # print list without the last index
# print(a[::-1])  # # print backwards
# print(a.index(3))  # # print index where 3 is at
# print(a[::2])  # # print every 2 indexes
del a[::2]  # delete item by coresponding indexes
div, mod = divmod(5, 2)  # Return quotient and remainder
# print(div, mod)
# method adds counter to an iterable and returns it (the enumerate object).
exam_first = enumerate(a, start=12)

# print(list(exam_first))


'''
Lambda in Python
'''

b = [1, 2, 3, 4, 5]


def x(a): return a + a
x_l = lambda a : a + a

lambda_exam = map(x_l, b)
# print(set(lambda_exam))

colors = ["Goldenrod", "purple", "Salmon", "turquoise", "cyan"]
# print(sorted(colors, key=lambda s: s.casefold()))
# print("Hello".casefold())

'''
Lambda can be problematic, just use def!
'''

def case_ignore(str): return str.casefold()
# print(sorted(colors, key=case_ignore))

'''
Conversions
'''

dict_exam = dict([(1,"Hi"), (2,"hello")])
# print(dict_exam)
join_exam = ["hello","world"]
out_first = ''.join(join_exam)
out_second = ':'.join(join_exam)
# print(out_first)
# print(out_second)

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
# print(ot)
# print(next(ot))
# print(next(ot))

li = iter([1,2,3])
# print(next(li)) #1
# print(next(li)) #2
# print(next(li)) #3
# # print(next(li)) #StopIteration

'''
List operation
'''

# 문자열 뒤집기
a = 'abc'
# print(a[::-1]) # 출력: cba

# 리스트 복사
a = [1, 2, 3]
b = a[:]
# print(b)      # 출력: [1, 2, 3]
# print(a is b) # 출력: False

c = [[1, 2], [3, 4]]
d = c[:]
c[0] = [5, 6] # 리스트 자체는 복사되지만
c[1][0] = 7   # 리스트의 원소들까지 복사되지는 않으므로 주의해서 사용하자.
# print(c)      # 출력: [[5, 6], [7, 4]]
# print(d)      # 출력: [[1, 2], [7, 4]]
# print('%s, %s, %s' % (c is d, c[0] is d[0], c[1] is d[1])) # 출력: False, False, True

'''
File IO
'''

# f = open("hello.txt", "w")
# try :
#     f.write("text")
# finally :
# #     f.close()

# class ManagedFile :
#     def __init__(self , name) :
#         self.name = name
    
#     def __enter__(self) :
#         self.file = open(self.name, "w")
#         return self.file
    
#     def __exit__(self , exc_type , exc_val , exc_tb) :
#         if self.file :
#             self.file.close()
            
# with ManagedFile("hello.txt") as f :
#     f.write("test")
#     f.write("test2")


'''
Useful Trick
https://m.blog.naver.com/passion053/221058266968
'''

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 1000 보다 작은 피보나치 수열을 출력
for i in fibonacci_generator():
    if i > 1000:
        break
    # print(i)

    a = (x * x for x in range(100))

# a 는 제너레이터 객체입니다. ( 역자 주: 아직 range(100) 은 실행되지 않은 상태 )
# print(type(a))

# 제너레이터의 값을 모두 더합니다.
# print(sum(a))

# 제너레이터에 값이 남아있지 않습니다.
# print(sum(a))

from collections import Counter

a = Counter('blue')
b = Counter('yellow')

# print(a)
# print(b)
# print((a + b).most_common(3))

a, *b, c = [2, 7, 5, 6, 3, 4, 1]
# print(a)
# print(b)
# print(c)

def cache(function):
    cached_values = {}  # 이미 계산된 값들만 저장합니다.
    def wrapping_function(*args):
        if args not in cached_values:
            # 인자값중 아직 저장되지 않은 값들에 대해서만 함수를 실행합니다.
            cached_values[args] = function(*args)
        return cached_values[args]
    return wrapping_function

@cache
def fibonacci(n):
    # print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print([fibonacci(n) for n in range(1, 9)])

from time import time


class Timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()
        return None  # could return anything, to be used like this: with Timer("Message") as value:

    def __exit__(self, type, value, traceback):
        elapsed_time = (time() - self.start) * 1000
        # print(self.message.format(elapsed_time))


with Timer("Elapsed time to compute some prime numbers: {}ms"):
    primes = []
    for x in range(2, 500):
        if not any(x % p == 0 for p in primes):
            primes.append(x)
    # print("Primes: {}".format(primes))

# print(any(a % 2==0 for a in range(0,10,2))) #return true


'''
read / work with excel
'''
import pandas as pd
import numpy as np

restaurant_file = pd.read_excel('flanb_data/file.xlsx', sheet_name='05.음식점(작업중)')

vendor_id_list = list(restaurant_file['vendor'])
vendor_uid_list = list(restaurant_file['vendor_uid'])

tag_start_count = 0
tag_finish_count = 0

for num in range(len(restaurant_file.columns)):
    if restaurant_file.columns[num].startswith('tag'):
        tag_start_count = num

    if restaurant_file.columns[num].startswith('openrice'):
        tag_finish_count = num
        break

temp_list = []
for i in range(tag_start_count, tag_finish_count):
    parsed_list = list(restaurant_file[restaurant_file.columns[i]].replace(np.nan, 'empty', regex=True))
    temp_list.append(parsed_list)
