def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    
    i = 0 

    while i < len(nums):
        product = 1
        j = 0
        while j < len(nums):
            if j == i:
                pass
            else:
                product *= nums[j]
            j += 1
            
        res.append(product)
        i += 1

    return res
