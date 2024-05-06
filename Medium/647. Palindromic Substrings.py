class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # he was saying that by checking left and right, we can determine if its a palindrome or not
        # i think we can reach an O(n^2) solution, at least 

        # for example... [r[a[c[e[c]a]r]b]c]
        # i think if we have a start and end index, and a next index to iterate through the string. on each iteration
        # we can check if left == right, if so, update local length. if greater that longest length, update that
        # keep expanding until reach end or start index
        # then increment our other index

        if len(s) == 1:
            return 1

        total = 0

        #deal with odd substrings, treating each index as the middle of a substr
        index = 0

        while index < len(s):
            l = index
            r = index
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    total += 1
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
                    total += 1
                    ll -= 1
                    rr += 1
                else:
                    break

            left += 1
            right += 1
        
        
        return total

