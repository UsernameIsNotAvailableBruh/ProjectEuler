import time

"""

a+b+c = 1000, a^2+b^2=c^2

c = 1000-(a+b)
c = sqrt (a^2+b^2)

1000-(a+b) = sqrt (a^2+b^2)

"""

def idk():
    for A in range(1, 500):
        for B in range(1, 500):
            if 1000-(A+B) == (A**2+B**2)**.5:
                return A*B*(1000-(A+B)), (A, B, (1000-(A+B))) 

s = time.perf_counter()
print(idk())
e = time.perf_counter()

print(e-s)