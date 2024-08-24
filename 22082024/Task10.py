number = int(input("Enter the integer number\n"))
fact = 1
if number < 0:
    print("Negative numbers are not allowed")
elif number == 1:
    print("The factorial of 1 is 1")
else:
    for i in range(1, number + 1):
        fact = fact * i
    print("The factorial of", number, "is", fact)
