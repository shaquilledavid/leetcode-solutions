"""
https://leetcode.com/problems/boats-to-save-people/

You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of
limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

def numRescueBoats(people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    
    """
    #approach here is to sort the list. then we pair the high weighing person with the low weighing person
    #if the high weight person can't be paired with anyone, he needs his own boat.
    
    people.sort()
    boats = 0
    start = 0
    end = len(people) - 1
    
    while start <= end:
        #case 1 where the pair is <= limit, add a boat and move on
        if people[start] + people[end] <= limit:
            boats += 1
            start += 1
            end -= 1
        
        else:
            #otherwise high is going to need their own boat
            boats += 1
            end -= 1
        
    return boats

    
    
