"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3762/

Given an array of strings products and a string searchWord. We want to design a
system that suggests at most three product names from products after each
character of searchWord is typed. Suggested products should have common prefix
with the searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord
is typed. 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],
        ["baggage","bags"],["bags"]]

"""
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        output = []
        matches = []

        i = 0
        j = 0
        letter = 0
        tmp = 0

        while i < len(products):
            while j < len(searchWord):
                while tmp < len(products):
                    if searchWord[0:j+1] == products[tmp][0:j+1]:
                        matches.append(products[tmp])
                        tmp += 1
                    else:
                        tmp += 1

                matches.sort()        
                output.append(matches[0:3])
                tmp = 0
                j += 1
                matches = []

            i += 1

        return output
            
