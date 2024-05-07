class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == ''.join([char for char in s[::-1]]):
            return s

        
        if len(s) == 1:
            return 1

        longest = s[0]

        #deal with odd substrings, treating each index as the middle of a substr
        index = 0

        while index < len(s):
            l = index
            r = index
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(longest):
                        longest = s[l:r+1]
                    
                    l -= 1
                    r += 1
                else:
                    break
            index += 1
        
        #now deal with the even substrings
        left = 0
        right = 1

        while right < len(s):
            ll = left
            rr = right
            while ll >= 0 and rr < len(s):
                if s[ll] == s[rr]:
                    if len(s[ll:rr+1]) > len(longest):
                        longest = s[ll:rr+1]

                    ll -= 1
                    rr += 1
                    
                else:
                    break

            left += 1
            right += 1
        
        
        return longest
