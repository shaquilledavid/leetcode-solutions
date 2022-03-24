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
    boats = 0 
    index = 0 
    spacesInCurrentBoat = 0
    capacity = 0
    
    people.sort()
    people.reverse()
    
    while index < len(people):
        if people[index] == limit:
            boats += 1
            index += 1
        
        elif index == (len(people) - 1) and capacity == 0:
            boats += 1
            index += 1
        
        else:
            j = index + 1
            spacesInCurrentBoat = 1
            capacity = people[index]
            while j < len(people) and spacesInCurrentBoat < 2:
                #case 2
                if capacity + people[j] <= limit:
                    capacity += people[j]
                    #remove that person so we dont encounter them again
                    people.remove(people[j])
                    spacesInCurrentBoat += 1
                
                else:
                    j += 1
                
            boats += 1
            index += 1
            capacity = 0
            spacesInCurrentBoat = 0
    
    
    return boats
    
