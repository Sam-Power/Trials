'''
Task
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
Input Format
A single line containing a string .
Constraints
Output Format
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
Sample Input
qA2
Sample Output
True
True
True
True
True
'''
if __name__ == '__main__':
    s = input()
    output = 0
    list_output = [False, False, False, False, False]
    #first line
    for i in s:
        if i.isalnum():
            list_output[0] = True
        if i.isalpha():
            list_output[1] = True
        if i.isdigit():
            list_output[2] = True
        if i.islower():
            list_output[3] = True
        if i.isupper():
            list_output[4] = True
    for a in list_output:
        print(a)