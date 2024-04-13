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
