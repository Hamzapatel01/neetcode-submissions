class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #use integer div and modulus to get the row and col
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n*m-1

        while (left<=right):

            mid = (right + left) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid+1
            else:
                right = mid -1

        return False
