class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = 0 
        R = len(numbers) - 1

        while L != R:
            total = numbers[L] + numbers[R]
            if total < target:
                L += 1
            elif total > target: 
                R -= 1
            else:
                return[L+1, R+1]
