import time

def idk(n):
    a = 0
    b = 0
    for x in range(n+1):
        a += x**2
        b += x
    return b**2-a    


s = time.perf_counter()
print(idk(100))
e = time.perf_counter()
b = e-s
print(b)