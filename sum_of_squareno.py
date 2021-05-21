
# Python Program for Sum of squares of first n natural numbers

n = int(input("enter a number"))
sm = 0
for i in range(1, n + 1):
    sm = sm + (i * i)
print(sm)