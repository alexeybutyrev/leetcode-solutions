# Problem: Find Positive Integer Solution for a Given Equation
# Language: python3
# Runtime: 384 ms
# Memory: 14.4 MB

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class customfunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        
        def search(x):
            hi = 1000
            lo = 1
            
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                
                if customfunction.f(x,mid) == z:
                    return mid
                if customfunction.f(x,mid) > z:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            if customfunction.f(x,lo) == z:
                return lo
            
            return -1
                
        for x in range(1,1001):
            y = search(x)
            if y >= 1:
                ans.append([x,y])
                    
        return ans