import time

def idk():
    x = 0
    while True:
        x+=2*3*4*5*6*7 #x+=2
        if (x%3==0 and x%4==0 and x%5==0 and x%6==0 and x%7==0 and x%8==0 and x%9==0 and x%10==0 and x%11==0 and x%12==0 and x%13==0 and x%14==0 and x%15==0 and x%16==0 and x%17==0 and x%18==0 and x%19==0 and x%20==0):
            return x


s = time.perf_counter()
print(idk())
e = time.perf_counter()
b = e-s
print(b)