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

# print(solution_2([3, 30, 34, 5, 9]))
# assert solution_2([3, 30, 34, 5, 9]), "9534330"

# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution_3(citations):
    c = sorted(citations)
    for idx, _ in enumerate(c):
        if c[idx] >= len(c)-idx:
            return len(c)-idx
    return 0

# from others,
# sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다. 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고, 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다. 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.

def solution_others(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# assert solution_3([3, 0, 6, 1, 5]), 3
# print(solution_3([3, 0, 6, 1, 5]))