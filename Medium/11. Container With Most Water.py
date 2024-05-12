def maxAreaBruteForce(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxArea = 0
    i = 0
    j = 1
    while i < len(height) - 1:
        while j < len(height):
            #case 1 equal heights
            if height[i] == height[j] or height[i] < height[j]:
                area = (j-i) * height[i]
            
            #case 2a/b differing heights 
            if height[j] < height[i]:
                area = (j-i) * height[j]
                
            if area > maxArea:
                maxArea = area
            
            j += 1

        i += 1
        j = i+1

    return maxArea

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxArea = 0
    left = 0
    right = len(height) - 1

    while left != right:
        short = min(height[left], height[right])
        area = short * (right-left)

        maxArea = max(maxArea, area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return maxArea
