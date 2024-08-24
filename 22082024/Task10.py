number = int(input("Enter the integer number\n"))
fact = 1
if number < 0:
    print("Negative numbers are not allowed")
elif number == 1 and number == 0:
    print("The factorial of 1 and 0 is 1")
else:
    for i in range(1, number + 1):
        fact = fact * i
    print("The factorial of", number, "is", fact)
