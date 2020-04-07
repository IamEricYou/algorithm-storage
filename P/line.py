def first_solution(inputString):
    start_bracket = ["[", "(", "<", "{"]
    close_bracket = ["]", ")", ">", "}"]
    temp_list = []
    
    for item in inputString:
        if item in start_bracket or item in close_bracket:
            temp_list.append(item)

    if len(temp_list) % 2 != 0:
        return -1
    
    count = 0
    comp_list = []
    for item in comp_list:
        if not temp_list:
            return count

        if item in start_bracket:
            idx = start_bracket.index(item)
            comp_list.append(1)
            if close_bracket[idx] in temp_list:
                comp_list.remove(1)
                temp_list.remove(item)
                temp_list.remove(close_bracket[idx])
                count += 1
            else:
                return -1
        else:
            if not comp_list:
                return -1
            idx = close_bracket.index(item)
            if start_bracket.index(start_bracket[idx]) > close_bracket.index(item):
                return -1


    if temp_list:
        return -1

    return count

value = "if (Count of eggs is 4.) {Buy milk.}"
value = "({)}"
value = "><"

print(first_solution(value))

def second_solution(road, n):
    ones = list(filter(None, road.split("0")))
    zeros = list(filter(None, road.split("1")))
    print(ones, zeros)


# road = "111011110011111011111100011111"
# n = 3 #should return 18
# second_solution(road, n)


def third_solution(dataSource, tags):
    answer = []
    matches = []
    for item in dataSource:
        for x in tags:
            if x in item and item[0] not in answer:
                match = set(item) & set(tags)
                answer.append(item[0])
                matches.append(len(tags) - len(match))

    answer = [x for _, x in sorted(zip(matches, answer))]
    return answer

def fourth_solution(directory, command):
    answer = []

    for item in command:
        if item.startswith("mkdir"):
            dest = item.split(" ")[1]
            directory.append(dest)

        if item.startswith("rm"):
            rm_item = item.split(" ")[1]
            temp_dir = directory.copy()
            for dirs in temp_dir:
                if dirs.startswith(rm_item):
                    directory.remove(dirs)

        if item.startswith("cp"):
            cp_item = item.split(" ")[2]
            cp_origin = item.split(" ")[1]
            for dirs in directory:
                if dirs.startswith(cp_origin):
                    directory.append(cp_item + dirs)
        print(directory)
    print(sorted(directory))
    return answer

# dataSource = [
#     ["doc1", "t1", "t2", "t3"],
#     ["doc2", "t0", "t2", "t3"],
#     ["doc3", "t1", "t6", "t7"],
#     ["doc4", "t1", "t2", "t4"],
#     ["doc5", "t6", "t100", "t8"]
# ]

# tags = ["t1", "t2", "t3"]

# print(third_solution(dataSource, tags)) 

directory = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]

command = [
"mkdir /root/tmp",
"cp /hello /root/tmp", 
"rm /hello"
]

result = [
"/", 
"/root", 
"/root/abcd", 
"/root/abcd/etc", 
"/root/abcd/hello", 
"/root/tmp", 
"/root/tmp/hello", 
"/root/tmp/hello/tmp"
]

directory = [
"/"
]

command = [
"mkdir /a",
"mkdir /a/b",
"mkdir /a/b/c",
"cp /a/b /",
"rm /a/b/c"
]

result = [
"/",
"/a",
"/a/b",
"/b",
"/b/c"
]

# fourth_solution(directory, command)

