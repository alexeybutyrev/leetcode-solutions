# Problem: Pascal's Triangle II
# Language: python
# Runtime: 20 ms
# Memory: 11.9 MB

class Solution(object):
    def f(self,v,l,n):
        
        if l == n:
            return v
        
        w = [1]
        for i in range(1,l):
            w.append(v[i-1] + v[i])
        
        w.append(1)
        return self.f(w,l+1,n)
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.f([1], 1, rowIndex+1)