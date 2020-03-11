#124 - print every possible number with 1,2,4

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n-1, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def solution(n):
    answer = []
    for x in ternary(n):
        if x == "0":
            x = 1

        elif x == "1":
            x = 2

        elif x == "2":
            x = 4

        answer.append(str(x))
        
    answer = ''.join(answer)
    return answer