def solution(p, s):
    answer = 13
    for i in range(0, len(p)):
        temp = int(p[i]) - int(s[i])
        if(temp < 0):
            temp = abs(temp)

        if(temp > 5):
            temp = 10 - temp
    answer = temp
    return answer


def solution_two(office, r, c, move):
    answer = 0
    move_count = 0
    move_flag = 1  # 1 up, 2 right, 3 down, 4 left
    total = office[r][c]
    office[r][c] = 0

    for item in move:
        if item == "go":
            save_r, save_c = r,c
            if move_flag == 1:
                r = r-1
                if(r < 0):
                    r = 0
                    continue

            if move_flag == 2:
                c = c+1
                if(c > len(office)-1):
                    c = c-1
                    continue

            if move_flag == 3:
                r = r+1
                if(r > len(office)-1):
                    r = r-1
                    continue

            if move_flag == 4:
                c = c-1
                if(c < 0):
                    c = 0
                    continue
            if office[r][c] == -1:
                r, c = save_r, save_c
                continue

            total = total + office[r][c]
            office[r][c] = 0

        if item == "right":
            move_flag += 1
            if move_flag == 5:
                move_flag = 1

        if item == "left":
            move_flag -= 1
            if move_flag == 0:
                move_flag = 4
                
    return answer

from itertools import combinations

def solution_three(numbers, K):
    answer = 0
    start = 0
    temp_idx = 0
    temp_arr = numbers.copy()
    # find_impossible = min(combinations(temp_arr, 2), key = lambda val: abs(val[0]-val[1]))
    # if(int(abs(find_impossible[0] - find_impossible[1])) > K):
    #     return -1
    print(min(combinations(temp_arr, 2), key = lambda val: abs(val[0]-val[1])))
    # while True:
    #     find_pair = min(combinations(temp_arr, 2), key = lambda val: abs(val[0]-val[1]))
    #     difference = int(abs(find_pair[0] - find_pair[1]))
    #     if answer == 1:
    #         break
    #     swap_val_first, swap_val_second = int(find_pair[0]), int(find_pair[1])
    #     temp_val, temp_idx = temp_arr[temp_arr.index(swap_val_first)], temp_arr.index(swap_val_second)
    #     temp_arr[temp_arr.index(swap_val_first)], temp_arr[temp_idx] = swap_val_second, temp_val
    #     answer += 1
    while answer < 5:
        
        temp_diff = []
        print(temp_arr)
        for i in range(0, len(temp_arr)-1):
            temp_diff.append(abs(temp_arr[i] - temp_arr[i+1]))
        if(max(temp_diff) < K):
            break
        max_idx, min_idx = temp_diff.index(max(temp_diff)), temp_diff.index(min(temp_diff))+1
        temp_swap = temp_arr[max_idx]
        temp_arr[max_idx] = temp_arr[min_idx]
        temp_arr[min_idx] = temp_swap
        print(temp_diff)
        print(temp_arr)
        answer += 1

    return answer


P = "82195"
S = "64723"  # 13
# solution(P,S)

office = [[5, -1, 4], [6, 3, -1], [2, -1, 1]]
r = 1
c = 0
move = ["go", "go", "right", "go", "right", "go", "left", "go"]  # 14

# solution_two(office, r, c, move)

numbers = [10, 40, 30, 20]
numbers = [3, 7, 2, 8, 6, 4, 5, 1]
k = 20 # 1
k = 3 # 2

solution_three(numbers, k)