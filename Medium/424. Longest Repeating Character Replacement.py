def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    charCount = {}
    L = 0
    maxLength = 0


    for R in range(len(s)):
        if s[R] in charCount:
            charCount[s[R]] += 1
        else:
            charCount[s[R]] = 1
            print(charCount)
            
        while len(s[L:R+1]) - max(charCount.values()) > k:
            print("entered")
            charCount[s[L]] -= 1
            L += 1


        maxLength = max(maxLength, len(s[L:R+1]))
        
    return maxLength
