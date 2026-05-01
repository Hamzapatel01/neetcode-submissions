class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #traverse through the array and put the numbers in the set
        #if you have already seen the numbers that means the number is a dup
        #else just keep adding if none found return false
        # the brute force would be sorting the nums array and checking if nums[i]==nums[i-1]
        # but the TC will become O(nlogn)
        
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        