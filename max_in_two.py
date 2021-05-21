# Maximum of two numbers in Python


choice = 'y'
while choice == 'y':
    num1 = float(input("enter first number : "))

    num2 = float(input("enter second number : "))

    if num1>num2:
        print(num1,"is max")
    else:
        print(num2, "is max")
    print("you want to check more")
    choice = input("enter y for yes or n for no")


    # maximum = max(num1, num2)
    # print(maximum)