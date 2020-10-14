import _ctypes
import csv

#This could be really danger, since it refers to the pointer
def di(obj_id):
    """ Inverse of id() function. """
    return _ctypes.PyObj_FromPtr(obj_id)

if __name__ == '__main__':
    # a = 42
    # b = 'answer'
    # print(di(id(a)))  # -> 42
    # print(di(id(b)))  # -> answer

    fileName = "hello.txt"
    crimefile = open(fileName, 'r')
    reader = csv.reader(crimefile)
    allRows = [row for row in reader]
    return_list = []
    for item in allRows:
        if not item:
            continue

        x = item[0]
        if x == 'TOPAS - TAG': 
            continue
        return_list.append(x)
    
    parsed = list(set(return_list))
    print(len(parsed))