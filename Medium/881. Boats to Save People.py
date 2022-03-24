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

    #new approach -> sort, check if person == limit. if they are, assign them a new boat. 
    #otherwise, check if the complement of that person is in the list. if they are, assign two to a boat,
    #otherwise, take next smallest person.
    
    people.sort()
    people.reverse()
    
    boats = 0
    index = 0
    while index < len(people):
        if people[index] == limit:
            boats += 1
            index += 1
        
        else:
            complement = limit - people[index]
            if complement in people:
                people.remove(complement)
                index += 1
                boats += 1
            
            else:
                #take the next smallest int from complement
                while complement > 0:
                    complement -= 1
                    if complement in people:
                        people.remove(complement)
                        boats += 1
                        index += 1
                        break
                
                #if that loop fully goes through and there is no person available to match, give the man his own boat    
                if complement == 0: 
                    boats += 1
                    index += 1
    
    return boats

    
    
