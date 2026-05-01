class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #traverse through the array and put the numbers in the set
        #if you have already seen the numbers that means the number is a dup
        #else just keep adding if none found return false

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        