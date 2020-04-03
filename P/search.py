#https://programmers.co.kr/learn/courses/30/lessons/42840

def first_solution(answers):
    first = [1,2,3,4,5] * len(answers)
    second = [2,1,2,3,2,4,2,5] * len(answers)
    third = [3,3,1,1,2,2,4,4,5,5] * len(answers)

    rank = [0,0,0]
    for index in range(0,len(answers)):
        if(first[index] == answers[index]):
            rank[0] += 1

        if(second[index] == answers[index]):
            rank[1] += 1

        if(third[index] == answers[index]):
            rank[2] += 1

    rankone = max(rank)
    return [i+1 for i, item in enumerate(rank) if item == rankone]
    return first


answers1 = [2,2,2,2,2] #required return [1]
answers2 = [1,3,2,4,2] #required return [1,2,3]

print(first_solution(answers1))