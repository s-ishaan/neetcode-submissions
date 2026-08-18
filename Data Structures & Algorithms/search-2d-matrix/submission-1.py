class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        t = m*n
        l = 0
        r = t-1

        while (l<=r):
            mid = l + ((r-l)//2)
            i = mid // m
            j = mid % m
            middle_value = matrix[i][j]
            if target == middle_value:
                return True
            elif target > middle_value:
                l = mid+1
            elif target < middle_value:
                r = mid-1
            
        return False