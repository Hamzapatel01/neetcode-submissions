from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for i in range(len(nums)):
            seen.add(nums[i])

        sorted_seen = sorted(seen)  # assign sorted list

        count = 1
        maxCount = 1
        if not sorted_seen:
            return 0
        for i in range(len(sorted_seen) - 1):  # prevent out-of-range
            if sorted_seen[i] + 1 == sorted_seen[i + 1]:
                count +=1
            else:
                count = 1
            maxCount = max(maxCount,count)

        return maxCount