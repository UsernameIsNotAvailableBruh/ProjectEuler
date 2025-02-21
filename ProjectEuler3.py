#Num = 13195
Num = 600851475143

def PrimeFactorsFinder(num:int):
    x = 2
    List = []
    while True:
        if num%x==0:
            num/=x
            List.append(x)
        x+=1
        if num == 1: break
    return List


print(max(PrimeFactorsFinder(Num)))