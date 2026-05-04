class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we can have a left pointer that will stuck at a point
        #we also have right pointer that will keep moving until we see a dup
        #make a set to keep track of all dups
        #whenever right pointer sees a dup it will look throughs et
        #and keep the left pointer +1 or we can have a while loop if there are more than1 consecutivee duplicates
        #time complexity - O(N) since we are at max traversing array only once
        #space complexity - O(N) because of set
        seen = set()
        left = 0
        maxCount = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            maxCount = max(i - left + 1, maxCount)
        return maxCount