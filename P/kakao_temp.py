import ast
import re

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"

def solution(s):
    s = s[1:-1]
    new = re.findall("\{(.*?)\}", eval(repr(s)))
    sorted_new = sorted(new, key=len)
    sorted_list = []
    answer = []
    for x in sorted_new:
        sorted_list.append(ast.literal_eval(x))

    count = 0
    answer.append(sorted_list[0])
    sorted_list.pop(0)
    for x in sorted_list:
      for y in x:
          if(y not in answer):
              answer.append(y)

    return answer

# print(solution(s))
# print(solution(s3))

n = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "abc1**"]
n1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b1 = ["fr*d*", "*rodo", "******", "******"]

import fnmatch
from itertools import groupby

def s_solution(n, b):
    answer = []
    count = 0
    temp = []
    possible = []

    for x in b:
        matches = fnmatch.filter(n, x)
        
        for item in matches:
            if(len(item) == len(x) and item not in temp):
                temp.append(item)
        possible.append(temp)
        temp = []

        print(possible)
        count = count + 1

   # print(count)

# s_solution(n1, b1)

def f_solution(stones, k):
    answer = 0
    new = stones
    while(True):
        new = [x - 1 if x > 0 else 0 for x in new]
        count = 0
        temp_list = [sum(1 for x in group if x == 0) for _, group in groupby(new)]
        temp_list = list(filter(lambda a: a != 0, temp_list))
        
        print(temp_list)
        if(k in temp_list):
            return answer + 1
        answer = answer + 1
    
    return answer

stone = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3

#print(f_solution(stone,k))

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def boardSolution(board, moves):
    answer = 0
    temp_list = []
    result_list = [-1]
    for x in moves:
        for y in board:
            if(y[x-1] != 0):
                temp_list.append(y[x-1])
                y[x-1] = 0
                break
    
    count = 0
    #print(temp_list)
    for i in range(len(temp_list)):
        if(result_list[-1] == temp_list[i]):
            del(result_list[-1])
            count += 1
            continue
        result_list.append(temp_list[i])
    answer = count * 2
    return answer

#print(boardSolution(board, moves))