### reverse a string and check it is a palindrom or not

def revpal(num):
    n = num
    result = 0 
    while num > 0:
        result = result * 10 + num % 10
        num = num //10
    print(f"reverse of the number {n} is {result}")
    print("palindrom" if result == n else "Not a Palindrom")

num = 1234321
revpal(num)