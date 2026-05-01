class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #check if the window we are at is valid
        #we can do this by checking if the length of window - max(freq) <=k
        #move the left pointer to right and decrement the count

        count = {}
        left = 0
        maxC = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
    
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]]-=1  
                left+=1

            maxC = max(maxC,right - left+1)
        return maxC
