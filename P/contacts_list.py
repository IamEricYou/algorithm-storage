# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(num):
    answer = True
    num = sorted(num, key=len)

    for prefix in num:
        num.pop(0)
        for item in num:
            print("item :" + str(item) + " num: " + str(num) + " prefix: " + str(prefix))
            if(item.startswith(prefix) and item != prefix):
                answer = False
                return answer
    return answer

def other_solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#https://programmers.co.kr/learn/courses/30/lessons/42588
def tower(height):
    answer = []
    reverse = height[::-1]
    for x in range(len(reverse)-1):
        if(reverse[x] < reverse[x+1]):
            answer.append()
    return answer


# set_first = ["12345", "12", "456", "7890"]
# set_second = ["123", "456", "789"]
# set_third = [ "234", "12345"]
# print(solution(set_first))
# print(solution(set_second))
# print(solution(set_third))

heights = [6,9,5,7,4]
print(tower[heights]) #returns [0,0,2,2,4]
heights = [3,9,9,3,5,7,2]
print(tower[heights]) #returns [0,0,0.3,3,3,6]
