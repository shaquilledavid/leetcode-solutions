def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    out = []
    hmap = {}

    #case 1 where 0 in nums to generate this type of triple
    i = 0
    if 0 in nums:
        while i < len(nums):

            if nums[i] == 0:
                i += 1
                pass
            
            triple = [nums[i], 0]
            inverse = 0 - nums[i]

            if nums[i] not in hmap:
                hmap[nums[i]] = i

            if inverse in hmap:
                triple.append(inverse)
                out.append(triple)

            i += 1


    #case 2 triples where 0 not involved
    print(hmap)



    index = 0
    while index < len(nums) - 1:
        j = index + 1
        while j < len(nums):
            total = nums[index] + nums[j]
            inverse = 0 - total
            if inverse in hmap and hmap[inverse] > j:
                triple = [nums[index], nums[j], inverse]
                if triple not in out:
                    out.append(triple)

            j += 1

        index += 1
        
    
    return out


print(threeSum([-1,0,1,2,-1,-4,-2]))
nums = [-1,0,1,2,-1,-4]
