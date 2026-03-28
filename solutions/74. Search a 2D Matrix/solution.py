# Problem: Search a 2D Matrix
# Language: python3
# Runtime: 40 ms
# Memory: 14.4 MB

from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        
        # search in row
        if n > 1:
            left, right = 0, n - 1
            while left != right-1:
                mid = left + (right - left) // 2
                #print(left,right, mid)
                if matrix[mid][0] == target:
                    return True
                if matrix[mid][0] < target:
                    left = mid
                else:
                    right = mid

            if matrix[left][0] == target:
                return True

            
            if target > matrix[left][m-1]:
                row = right
            elif target == matrix[left][m-1]:
                return True
            else:
                row = left
        else:
            row = 0
            
        
        left, right = 0, m 
        while left != right -1:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid
            else:
                right = mid
        
        if matrix[row][left] == target:
            return True
        
        #if matrix[row][right] == target:
        #    return True

        return False
    
        