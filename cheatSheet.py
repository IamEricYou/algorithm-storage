#!/user/bin/env python

#Basic list Operation

a = [1,2,3,4,5]
print(a[:-1]) #Print list without the last index
print(a[::-1]) #print backwards
print(a.index(3)) #print index where 3 is at
print(a[::2]) #print every 2 indexes
del a[::2] #delete item by coresponding indexes
print(a)