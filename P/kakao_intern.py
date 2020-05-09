def get_distance(finger, target):
    L = [1, 4, 7] # 1
    R = [3, 6, 9]
    either = [2, 5, 8, 0] # 2

    if finger in L:
        idx = L.index(finger)
        return abs(either.index(target) - idx) 

    if finger in R:
        idx = R.index(finger)
        return abs(either.index(target) - idx) 

    if(finger in either):
        return abs(either.index(target) - either.index(finger))

    return -1 

def solution(numbers, hand):
    answer = ""
    L = [1, 4, 7] # 8 -> 0 = 1
    R = [3, 6, 9] # 9 -> 5 = 1
    either = [2, 5, 8, 0]

    left_hand_location = 0
    right_hand_location = 0

    for item in numbers:
        if item in L:
            answer += "L"
            left_hand_location = item

        if item in R:
            answer += "R"
            right_hand_location = item

        if item in either:
            if right_hand_location in either:
                right_diff = abs(either.index(right_hand_location) - either.index(item))
                if right_diff == 1:
                    right_diff = 0     
            else:
                right_diff = abs(R.index(right_hand_location) - either.index(item))
            
            if left_hand_location in either:
                left_diff = abs(either.index(left_hand_location) - either.index(item) )
                if left_diff == 1:
                    left_diff = 0        
            else:
                left_diff = abs(L.index(left_hand_location) - either.index(item))

            if right_diff > left_diff:
                answer += "L"
                left_hand_location = item
            
            if right_diff < left_diff:
                answer += "R"
                right_hand_location = item
            
            if right_diff == left_diff:
                if hand == "right":
                    answer += "R"
                    right_hand_location = item
                else:
                    answer += "L"
                    left_hand_location = item

    return answer


def two(expression):
    import re
    temp = re.split('(\d+)',expression)
    operation_list = list(filter(None, temp))

    answer = []
    operator_priority_list = [
        "+-*",
        "-+*",
        "*-+",
        "+*-",
        "*+-",
        "-*+"
    ]

    for item in operator_priority_list:
        temp_list = operation_list.copy()
        for sign in item:
            if sign not in temp:
                continue
            while True:
                if sign not in temp_list:
                    break

                idx = temp_list.index(sign)
                first_value = int(temp_list[idx-1])
                second_value = int(temp_list[idx+1])

                if sign == "+":
                    temp_list[idx] = first_value + second_value

                if sign == "-":
                    temp_list[idx] = first_value - second_value

                if sign == "*":
                    temp_list[idx] = first_value * second_value
                
                del(temp_list[idx-1])
                del(temp_list[idx])
            answer.append(abs(int(temp_list[0])))

    return max(answer)

def check_apeche_has_all(compare, target):
    for item in target:
        if item not in compare:
            return False
    return True

def three(gems):
    answer = []
    delete_duplicates = list(set(gems))
    count = 1
    temp_list = []

    for i in range(len(gems)):
        temp_list.append(gems[i])
        if check_apeche_has_all(temp_list,delete_duplicates):
            break

    last_idx = len(temp_list)
    comp_list = temp_list.copy()
    for item in temp_list:
        comp_list.remove(item)
        if item not in comp_list:
            break
        count += 1

    return [count, last_idx]

def different_three(gems):
    answer = [1,1]
    delete_duplicates = list(set(gems))
    if len(delete_duplicates) == 1:
        return answer

    temp_list = []
    count = len(delete_duplicates)
    idx_count = 0

    for item in gems:
        if count == 0:
            answer[1] = idx_count 
            break

        if(item not in temp_list):
            count -= 1

        temp_list.append(item)
        idx_count += 1
    
    if count == 0 and idx_count == len(gems):
        answer[1] = idx_count 

    idx_count = 1
    copy_list = temp_list.copy()
    for item in temp_list:
        if(copy_list.count(item) > 1):
            copy_list.remove(item)
            idx_count += 1
            continue
        break

    answer[0] = idx_count
    return answer

def maze(n, path, order):
    visited = []
    # for item in order:
    return n


def board(boards):
    answer = []

    for i in range(len(boards)):
        for j in range(len(boards)):
            print(boards[i][j])

    return answer

print(solution( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LRLLLRLLRRL" 
# print(two("100-200*300-500+20")) # 60420
# print(different_three(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
# print(different_three(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]
# print(board([[0,0,0],[0,0,0],[0,0,0]]))
# print(maze(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])) # true

# [[4,1],[8,7],[6,5]]