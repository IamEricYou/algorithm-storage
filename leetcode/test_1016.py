def solutions(registered_list, new_id):
    import re
    legit = True
    answer = ''
    m = re.search(r"\d", new_id)
    # see if number starts before index 3
    if m and m.start() < 3:
        legit = False
    
    if m:
        new_id_first = new_id[:m.start()]
        new_id_last = new_id[m.start():]
        if new_id_last[0] == '0':
            legit = False
    else:
        new_id_first = new_id
    # see if string contains any uppercase
    legit = any(c.islower() for c in new_id_first)
    print(legit)
    return answer
    

def solution(registered_list, new_id):
    import re
    answer = ''
    if new_id in registered_list:
        number_index = re.search(r"\d", new_id)
        if number_index:
            new_id_string = new_id[:number_index.start()]
            new_id_number = int(new_id[number_index.start():])
        else:
            new_id_string = new_id
            new_id_number = 1
        
        for r in sorted(registered_list):
            print(r)
            if r == f"{new_id_string}{new_id_number}":
                new_id_number += 1
                answer = f"{new_id_string}{new_id_number}"
            else:
                answer = f"{new_id_string}{new_id_number}"
                continue
    else:
        answer = new_id
    return answer

r = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
n = "cow"
print(solution(r,n))