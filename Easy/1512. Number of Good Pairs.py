def numIdenticalPairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    i = 0
    while i < len(nums):
        d[i] = []
        for num in nums[i+1:]:
            if num == nums[i]:
                d[i].append(num)
                
        i += 1
        

    return sum(len(value) for value in d.values())


def numIdenticalPairs2(self, nums):
    numseen = []
    count = 0
    for num in nums:
        if num not in numseen:
            count_of_number = nums.count(num)
            count += count_of_number * (count_of_number - 1) // 2
            numseen.append(num)    
        else:
            pass
        
    return count
