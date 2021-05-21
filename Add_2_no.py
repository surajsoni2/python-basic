# Python program to add two numbers

choice = 'y'
while choice == 'y':
    num1 = int(input("enter first number : "))

    num2 = int(input("enter second number : "))
    print("sum = :",num2+num1)
    print("you want to add more")
    choice = input("enter y for yes or n for no")