# Problem: Find Smallest Common Element in All Rows
# Language: python
# Runtime: 552 ms
# Memory: 37 MB

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        c = Counter()
        
        for m in mat:
            for a in m:
                c[a] += 1
                if c[a] == len(mat):
                    return a
        
        return -1