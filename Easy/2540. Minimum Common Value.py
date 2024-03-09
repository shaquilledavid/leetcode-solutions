class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # [1,3,4,23]    [0,2,4]
        if max(nums1) > max(nums2):
            smaller = nums2
            larger = nums1                                                           
    
        else:
            smaller = nums1
            larger = nums2

        minimum = -1

        i = 0
        j = 0 

        while j < len(smaller):
            if smaller[j] > larger[i]:
                i += 1
            
            elif smaller[j] < larger[i]:
                j += 1
            
            elif smaller[j] == larger[i]:
                return smaller[j]
        
        return minimum
