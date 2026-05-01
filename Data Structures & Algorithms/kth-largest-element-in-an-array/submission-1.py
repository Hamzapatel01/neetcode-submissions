class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we need to return the k largest integer including duplicates
        # so what we can do here is that we can have a min heap
        # and we keep popping until we have len(heap) == k
        # return the top once done

        heapq.heapify(nums)

        while len(nums) > k:

            heapq.heappop(nums)

        
        return nums[0]