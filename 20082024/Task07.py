# Task: Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

# Take the input from the user
year = int(input("Enter the year\n"))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"The {year} is Leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"The {year} is a leap year")
else:
    print(f"The {year} is not a leap year")
