"""
Try Exponent Sorting Practice
"""
import math

def findScheduleConflicts(arr):
    """
    Returns a list of all the unique appointments that are in conflict with each
    other.
    """
    #brute force approach -> comparing each appointment in the list
    #a conflict will occur if the start time of 2nd appt is in range or end time of 2nd appt is in range

    conflicts = []
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j][0] in range(arr[i][0], arr[i][1]) or arr[j][1] in range(arr[i][0]+1, arr[i][1]):
                conflicts.append(arr[i])
                conflicts.append(arr[j])
            j += 1

        i += 1
        j = i + 1

    return conflicts


x =[[2,3], [1,2], [3,5], [4,6]]


def findScheduleConflicts_SORTED(arr):
    """
    Use sorting to help us approach this question better
    """
    arr.sort()
    conflicts = []
    i = 1
    while i < len(arr):
        if arr[i][0] in range(arr[i-1][0], arr[i-1][1]):
            conflicts.append(arr[i-1])
            conflicts.append(arr[i])
        i += 1
        
    return conflicts

################################################################################

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]

def findDuplicates(arr1, arr2):
    """
    Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates
    that returns an array of all passport numbers that are both arrays. Note that the output array
    should be sorted in ascending order.

    >>> findDuplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])
    [3, 6, 7]
    """

    #brute force: go through all elements in arr 1, see if they are in arr2, then append
    duplicates = []
    for number in arr1:
        if number in arr2:
            duplicates.append(number)

    return duplicates

def findDuplicates_SORTED(arr1, arr2):
    """
    Approach using pointers in each array
    """
    duplicates = []
    if len(arr1) < len(arr2):
        shorter = arr1
        longer = arr2
    else:
        shorter = arr2
        longer = arr1
    
    
    i = 0
    j = 0
    while i < len(longer):
        if shorter[j] == longer[i]:
            duplicates.append(shorter[j])
            j += 1
            i += 1

        elif shorter[j] > longer[i]:
            i += 1

        else:
            j += 1

    return duplicates

        
def findDuplicates_BinarySearch(arr1, arr2):
    #we want to use Binary search when one array is significanly larger than another
    #therefore, we don't have to traverse the large array completely, we can break it down into pieces

    if len(arr1) > len(arr2):
        longer = arr1
        shorter = arr2
    else:
        longer = arr2
        shorter = arr1

    duplicates = []

    for number in shorter:
        #use binary search to check if it is in the longer array
        if binarySearch(longer, number) != -1:
            duplicates.append(number)

    return duplicates

def binarySearch(array, number):
    #Helper function that will use binary search to return if number is in array

    begin = 0
    end = len(array) - 1

    while begin <= end:
        mid = begin + math.floor((end-begin)/2)     #NOTE the implementation of mid must be this 

        if array[mid] == number:
            return array[mid]

        elif number < array[mid]:
            end = mid - 1

        else:
            begin = mid + 1

    return -1

################################################################################

def find_first(array, num):
    """
    Returns the index at which the number num first appears in the input array

    >>> find_first([200, 200, 200, 200, 500, 500, 500])
    4
    """


    #we know that the array is sorted so we can use binary search to our advantage
    #to find the FIRST occurence of a num, we need to continue searching the left side of when we find an occurence

    begin = 0
    end = len(array) - 1
    index = -1

    while begin < end:
        mid = begin + math.floor((end-begin)/2)

        if array[mid] == num:
            #update the index
            index = mid
            end = mid
            continue

        elif array[mid] < num:
            begin = mid + 1
            continue

        elif array[mid] > num:
            end = mid
            continue

    return index
