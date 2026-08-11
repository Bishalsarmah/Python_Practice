def fac(num):
    res=[]
    for i in range(1,int((num)**0.5)+ 1):   ##num**0.5 is for square root we can simply import math sqrt also
        if num%i == 0:
            res.append(i)
            if num // i != i:
                res.append(num//i)
    res.sort()
    return res

num = 36
print(fac(num))
