class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        L = 1
        R = 1

        while R < len(nums):
            #if r = r-1 -> r += 1
            #else, nums[L] = R, L += 1 R += 1
            if nums[R] == nums[R-1]:
                R += 1
            
            else:
                nums[L] = nums[R]
                R += 1
                L += 1
            
        return L

# neetcode two pointer explanation: https://www.youtube.com/watch?v=DEJAZBq0FDA
# my intial approach -> using one pointer, comparing i with i-1. popping if same, moving on if different.
