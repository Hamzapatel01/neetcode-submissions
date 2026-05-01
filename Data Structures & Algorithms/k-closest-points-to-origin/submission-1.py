class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # can use a min heap to store the closest min dist
        # heapify the dist
        distlist = []
        for i in range(len(points)):
            x,y = points[i]

            dist = math.sqrt(x**2+y**2)
            distlist.append([dist, points[i]])
        heapq.heapify(distlist)
        result = []
        #remove the largest distance
        for i in range(k):
            result.append(heapq.heappop(distlist)[1])
        return result        