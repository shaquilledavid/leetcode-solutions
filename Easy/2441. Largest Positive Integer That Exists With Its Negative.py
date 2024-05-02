class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxK = -1

        i = 0 
        while i < len(nums):
            if nums[i] < 0 and abs(nums[i]) in nums and maxK < abs(nums[i]):
                    maxK = abs(nums[i]) 
            i += 1

        return maxK
