"""
Ashley loves numbers made up of unique digits. She is less enchanted with numbers
that have repeating digits. Given a range of integers, determine how many number
s she will love. For example, the lower bound n=80 and the upper bound m=120.
Both are inclusive, so there are 120-79=41 values in the range.

Complete the function countNumbers.

"""

def countNumbers(rangeArray):
    allnums = []
    for num in range(rangeArray[0], rangeArray[1] + 1):
        allnums.append(num)

    uniqueNumbers = []
    for number in allnums:
        if allUnique(number) == True:
            uniqueNumbers.append(number)
        else:
            pass

    return len(uniqueNumbers)


def allUnique(number):
    num = str(number)
    seen = []
    for digit in num:
        if digit in seen:
            return False
        else:
            seen.append(digit)

    return True
