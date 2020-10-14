import time

t0 = time.time()
for i in range(0,100000000):
    a = i
t1 = time.time()

total = t1-t0
print(f"{total} .. ")
