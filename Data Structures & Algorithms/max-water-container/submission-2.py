class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #pick widest width for max area
        #assign two pointers left and right and 
        #if the left pointer height is less than right pointer height
        #take left one and move left++ and check for th width again
        # if this new updated width is larger than prev one
        # update that with thte new width we found and check for the height too while updating
        # using max (area,area_prev)
        #take the min of two heights so that no height bar could be shorter
        #then compute area


        left = 0
        right = len(heights)-1
        area = 0 
        while(left<right):

            width =  right - left
            curr = min(heights[right],heights[left]) * width
            area = max(area,curr)
            if (heights[left]<heights[right]):
                left+=1
            else:
                right -=1

        return area
