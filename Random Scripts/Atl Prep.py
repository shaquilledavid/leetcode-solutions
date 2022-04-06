"""
Write a function that accepts a string of numbers and a positive integer as an argument. The function should reduce the string in the following way:

EXAMPLE:
reduceTheNumber(numberString, k)

Input:
"1111123212", 3

Output:
"132"

Step 1
Split the numberString into as many groups of size k as possible, the remaining
number(s) should placed in their own grouping.

So for our example, there will be 3 full groupings and 1 leftover grouping.*

"1111123212"  
[111]  [112]  [321]  [2]
Step 2
Sum each grouping

[1+1+1]  [1+1+2]  [3+2+1]  [2]
[3] [4] [6] [2]
Step 3
Repeat Steps 1 and 2, grouping and summing until you are left with only k numbers

[3 ] [4] [6] [2]
[3 4 6] [2]
[3 + 4 + 6] [2]
[13][2]
Step Four
When you are left with only k digits, return the numbers as a string.

[13][2]
=> "132"
"""

def reduceTheNumber(numberString, k):
    if k > len(numberString):
        return numberString

    while len(numberString) > k:
        numberString = groupAndSum(numberString, k)

    return numberString


def groupAndSum(numstring, k):
    groups = []
    i = 0
    while i < len(numstring):
        groups.append(numstring[i:i+k])
        i += k

    s = ''
    for group in groups:
        num = 0
        for digit in group:
            num += int(digit)
        s+= str(num)

    return s
