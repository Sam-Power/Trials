"""Task:
Find out if a given number is an "Armstrong Number".
An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
371 = 33 + 73 + 13;
9474 = 94 + 44 + 74 + 44;
93084 = 95 + 35 + 05 + 85 + 45.
Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values then display a warning message to the user."""
number = input("Please enter an integer number: ")
power = len(number)
sonuc = 0
if number.startswith("-") or "." in number or "," in number or (not number.isdigit()):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in number:
        sonuc += int(i) ** power
    if int(number) == sonuc:
        print(number + " is an Armstrong number")
    else:
        print(number + " is not an Armstrong number")
