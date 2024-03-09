class Solution(object):
    def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    duplicates = []
    for number in nums1:
        if number in nums2 and number not in duplicates:
            duplicates.append(number)

    return duplicates
