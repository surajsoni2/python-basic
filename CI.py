# Python Program for compound interest


choice = 'y'
while choice == 'y':
    p = int(input("enter principle amount "))
    t = int(input("enter Time Period "))
    r = int(input("enter rate of interest "))
    Amount = p * (pow((1 +  r/ 100), t))
    CI = Amount - p
    print("Compound interest is", CI)
    print("you want to check more")
    choice = input("enter y for yes or n for no ")
