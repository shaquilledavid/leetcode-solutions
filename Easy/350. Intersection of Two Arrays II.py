class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        duplicates = []
        if len(nums1) > len(nums2):
            larger = nums1
            smaller = nums2
        else:
            larger = nums2
            smaller = nums1

        for number in larger:
            if number in smaller:
                index = smaller.index(number)
                duplicates.append(number)
                smaller.pop(index)

        return duplicates
