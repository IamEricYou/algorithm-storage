import _ctypes

#This could be really danger, since it refers to the pointer
def di(obj_id):
    """ Inverse of id() function. """
    return _ctypes.PyObj_FromPtr(obj_id)

if __name__ == '__main__':
    a = 42
    b = 'answer'
    print(di(id(a)))  # -> 42
    print(di(id(b)))  # -> answer