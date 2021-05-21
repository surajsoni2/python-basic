# Python Program to check Armstrong Number

num = int(input(("enter a number to check")))

mylst = list(str(num))
no_Of_Power = len(mylst)

total_digit_cubesum = 0
for x in mylst:
    total_digit_cubesum += pow(int(x),no_Of_Power)
if num == total_digit_cubesum:
    print(num," is Armstrong number")
else:
    print(num, " is not Armstrong number")


# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")