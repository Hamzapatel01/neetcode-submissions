class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find mid 
        #smallest element will be the first num of a rotated arrya

        #look at the num[mid] if that is larger than nums[right]
        #the number lies on the right side perform binarysearch on that
        #set left pointer to mid+=1 and right doesnt change

        #if num[mid]is less than nums[right] then number lies in thef ront
        #we can just do normal bs and return left

        left = 0
        right = len(nums) - 1

        while left<right:

            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                #numebr on left
                right = mid 

                
        return nums[left]