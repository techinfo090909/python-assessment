
# Question 3: Sum of Numbers from 1 to N

n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    total = 0

    for i in range(1, n + 1):
        total = total + i

    print("Sum is:", total)
