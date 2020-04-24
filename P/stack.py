# https://programmers.co.kr/learn/courses/30/lessons/42586

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
progress = [93, 30, 55]
speed = [1, 30, 5]  # required return = [2,1]

#print(solution_first(progress, speed))

# https://programmers.co.kr/learn/courses/30/lessons/42583


import queue
def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp_weight = weight
    waited_truck = queue.Queue()
    [waited_truck.put(x) for x in truck_weights]
    passing_truck = queue.Queue()
    for item in truck_weights:
        passing_truck.put(item)
        temp_weight 
    passed_truck = queue.Queue()
    count_time = 1
    

    print(list(waited_truck.queue))
    while(not passing_truck.empty()):
        count_time += 1
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6] # 8 

solution(bridge_length, weight, truck_weights)
