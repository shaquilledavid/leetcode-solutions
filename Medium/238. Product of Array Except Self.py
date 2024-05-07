def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    res = []
    index = 0 

    
    #compute the prefix and postfix products at each
    prefix = [1]
    postfix = [1]
    product = 1

    #prefix work
    while index < len(nums):
         product *= nums[index]
         prefix.append(product)
         index += 1
        
    #postfix work
    prod = 1
    ind = len(nums) - 1
    while ind >= 0:
        prod *= nums[ind]
        postfix.insert(0, prod)
        ind -= 1
        #value going into the result array at each index with be the product of the prefix at index*postfix at index+1

    n = 0
    while n < len(nums):
        res.append(prefix[n]*postfix[n+1])
        n += 1

    return res
