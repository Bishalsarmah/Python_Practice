#counting no of digits in a number 

def counting(num):
    n = num
    count = 0 
    while num>0:
        count += 1
        num = num //10
    print(f"No of digits in {n} is {count}")

num = int(input("Enter a number "))
counting(num)