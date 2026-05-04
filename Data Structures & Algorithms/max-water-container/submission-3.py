class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #pick the widest width which will be 0 to n
        #make two pointers to track the height one will comapre it to track the min he
        #keep storing width times height into an varaiba;e
        #now keep moving the left pointer to right
        #do we need to move according to the min height?
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while left<right:
            width = right - left
            height = min(heights[left], heights[right])
            area = height*width
            maxArea = max(maxArea,area)
            print(maxArea)
            if heights[left] < heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return maxArea