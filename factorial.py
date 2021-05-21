# Python Program for factorial of a number

choice = 'y'
while choice == 'y':
    num1 = int(input("enter a number "))
    fact = 1
    if num1 < 0:
        print("factorial is not possible for negative numbers")
    elif num1 == 0 or num1 ==1:
        print("factorial of ",num1,"is 1")
    else:
        for x in range(2,num1+1):
            fact = fact*x
        print("factorial of ",num1,"is",fact)
    print("you want to check more")
    choice = input("enter y for yes or n for no ")




