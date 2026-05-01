class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return k closest points to the origin
        # check for the distance by using the formula they give
        # we can access the x and y by using a nested loop
        distlist = []
        for i in range(len(points)):
            x,y = points[i]
            dist = math.sqrt(x**2 + y**2)
            print(dist)

            distlist.append([dist,points[i]])

        distlist.sort()
        result = []

        for i in range(k):
            result.append(distlist[i][1])
            
        return result