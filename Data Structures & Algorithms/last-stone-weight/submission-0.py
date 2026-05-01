class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we will use a max heap just to keep the two maximum weight
        # we can heapify this to conevrt to heap and multiply with -1
        # push back  the difference
        # keep doing it until curr_idx < len(stones)
        # return the top of the heap if there is one if not then return 0

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            x = -heapq.heappop(stones) #store the largest
            y = -heapq.heappop(stones) #store the second largest
            if x!=y:
                heapq.heappush(stones, y-x) #this case also handles x == y since it will be 0

        return -stones[0] if stones else 0

        
