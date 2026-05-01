class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # to find the target what we could do is split the array and find mid
        # if mid num is less than target is on right so move left pointer on mid+1

        left = 0
        right = len(nums)-1
        while (left<=right):

            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid -1

        return -1
