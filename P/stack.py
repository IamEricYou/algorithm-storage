#https://programmers.co.kr/learn/courses/30/lessons/42586

import math 
def solution_first(progress, speed):
    answer = [1]
    complete_days = [math.ceil((100 - x) / y) for x, y in zip(progress, speed)]
    print(complete_days)
    for j in range(1, len(complete_days)):
        if (complete_days[j] > complete_days[j-1]):
            answer.append(1)
        else:
            answer[j-1] = answer[j-1] + 1
    return answer

[7, 12, 9]
progress = [93,30,55]
speed = [1,30,5] #required return = [2,1]

print(solution_first(progress, speed))
