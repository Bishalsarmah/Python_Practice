### check a number is armstrong no or not

def arm(num):
    n = num
    # ori = num
    l = len(str(num))
    res = 0
    while n > 0 :
        res = res + (n % 10)**l
        n = n // 10
    print("Armstron" if res == num else "Not a Armstrong number")

num = 154
arm(num)

