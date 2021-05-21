# Python program to check whether a number is Prime or not


num = int(input(("enter a number to check")))

for x in range(2,num):
    if num%x == 0:
        print(num,"is not prime")
        break
    elif x==num-1:
        print(num,"is prime")
        break