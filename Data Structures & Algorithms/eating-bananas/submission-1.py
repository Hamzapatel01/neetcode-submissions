class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left<=right:

            mid = (left+right)//2  #mid here represents k rate
            hours = 0

            for num in piles:
                hours += math.ceil(num/mid)
                
            if hours <= h:
                right = mid-1
            else:
                left = mid+1

        return left