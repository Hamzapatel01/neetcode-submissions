class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # the brute force appraoch will be to put wvwrything in a set
        #if you have seen the number in the set that means it is a dup
        # lower side is that it is O(N) space and linear Tc
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return 0
        