class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #put the string char into set 
        #once you encounter a char that is alr in set
        #reduce count
        #

        strs = set()
        left = 0 
        maxC = 0

        for right in range(len(s)):
            while s[right] in strs:
                strs.remove(s[left])
                
                left+=1

            strs.add(s[right])
            maxC = max(maxC,right-left+1)

        return maxC
