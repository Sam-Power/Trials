"""Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.
The examples of the desired output are as follows :
input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number"""
x = int(input("Enter a number to check whether it is Prime number or not: "))
divider = 0
for i in range(2,x):
    if x % i == 0:
        divider += 1
        break
if divider == 0:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")



