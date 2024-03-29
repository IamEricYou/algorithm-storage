# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter

def solution(clothes):

    counter_each_category = Counter([cat for _, cat in clothes])
    all_possible = 1
    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)
        return all_possible - 1


a = 14 + 7
b, _, c = 1, 2, 3

print(b,c) #print 1,3