
# Dynamic Programming
# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    count = 1 
    answer = 0
    temp = [0, {N}]
    print(temp)
    saved = [] 
    while True:
        saved_val = 0
        if not saved_val in saved:
            saved.append(saved_val)
        
        if (count == 9):
            break
        
        print(count)
        count += 1
    # 원소별로 도는횟수 저장해서 출력하는거.. (생각보다 효율적이진 않을거같음..)
    return answer


N = 5
number = 12 # 4
# N = 2 
# number = 11 # 3

solution(N, number)

# 1463
# https://lee-seul.github.io/algorithm/2017/03/16/dynamic-programming.html
x = int(input())

dp = [0 for _ in range(x+1)]
dp[1] = 0

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[x])