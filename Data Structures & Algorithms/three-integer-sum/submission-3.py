class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #comapre 1st and 2nd elemtn with n-1 
        #subtract one from end to the left and move to the right the second pointer

        #sort the array and then lock the first index and 
        #compare wuth the next and last index 
        #if the sum is greater than 0 that means the number should be on left
        #so we do right -- and if sum is less than 0 then we do left++
        #but we also check if prev and current value are same so we skip

        nums.sort()
        res = []

        for i in range(len(nums)):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1

            while(left<right):
                

                if (nums[left]+nums[right]+nums[i] == 0):
                    res.append([nums[left],nums[right],nums[i]])
                    right-=1
                    left+=1
                    while (left<right and nums[left] == nums[left-1]):
                        left+=1
                    while(left<right and nums[right] == nums[right+1]):
                        right-=1
                    
                elif (nums[left]+nums[right]+nums[i]<0):
                    left=left+1
                elif (nums[left]+nums[right]+nums[i] > 0):
                    right = right - 1

        return res