# Python Program for simple interest
choice = 'y'
while choice == 'y':
    p = int(input("enter principle amount "))
    t = int(input("enter Time Period "))
    r = int(input("enter rate of interest "))
    
    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    print("you want to check more")
    choice = input("enter y for yes or n for no ")



