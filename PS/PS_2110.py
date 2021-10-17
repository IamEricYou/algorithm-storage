#https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution_1(array, commands):
    answer = []
    for c in commands:
        print(array[c[0]-1:c[1]])
        l = sorted(array[c[0]-1:c[1]])[c[2]-1]
        answer.append(l)
    return answer

# assert solution_1([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5, 6, 3]

# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution_2(numbers):
    num = [str(i) for i in numbers]
    return str(int(''.join(sorted(num, key=lambda i: i*10, reverse=True))))

print(solution_2([3, 30, 34, 5, 9]))
assert solution_2([3, 30, 34, 5, 9]), "9534330"