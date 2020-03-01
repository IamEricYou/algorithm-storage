#!/usr/bin/env python3

# https://programmers.co.kr/learn/courses/30/lessons/12928
def sumDivisor(num):
    return sum(i for i in range(1, num+1) if num % i == 0)

def getMinSum(A,B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

# https://programmers.co.kr/learn/courses/30/lessons/12916
def numPY(s):
	return s.count('p') + s.count('P') == s.count('Y') + s.count('y')

# https://programmers.co.kr/learn/courses/30/lessons/12906
def no_continuous(s):
    from itertools import groupby
    return [x[0] for x in groupby(s)]

#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for x,y in zip(participant, completion):
        if x != y:
            return x
    return participant[-1]


if __name__ == '__main__':
    print(int(12/19 + 3/1))