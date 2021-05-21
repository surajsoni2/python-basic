# import sympy
#
# print(list(sympy.primerange(0, 500)))
#
first = int(input("enter th first number from to print prime's"))
last = int(input("enter th last number from to print prime's"))
for num in range(first,last):
    for x in range(2,num):
        if num%x == 0:
            break
        elif x==num-1:
            print(num)
            break