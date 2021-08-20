# https://programmers.co.kr/learn/courses/30/lessons/83201


def grade_calculator(score):
    grade = ""
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade

def solution_1(scores):
    trasnsposed_list = list(map(list, (zip(*scores))))
    grades = ""
    for idx, score in enumerate(trasnsposed_list):
        # 자기 점수가 최고점이나 최저점이라면
        s = score
        if s[idx] in (max(score), min(score)):
            if score.count(s[idx]) > 1:
                pass
            else:
                del s[idx]
                
        avg = sum(s) / len(s)
        grades += grade_calculator(avg)
        
    return grades

# "FBABD"
# d = solution_1([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],
#               [61,57,100,80,65],[24,90,94,75,65]])


# https://programmers.co.kr/learn/courses/30/lessons/82612'

def solution_2(price, money, count):
    return sum([price * num for num in range(1, count+1)]) - money if sum([price * num for num in range(1, count+1)]) - money > 0 else 0

# 4
# d = solution_2(3, 20, 4)


# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution_3(lottos, win_nums):
    answer = []
    return answer

# [3, 5]
d = solution_3([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
print('d: ', d)
