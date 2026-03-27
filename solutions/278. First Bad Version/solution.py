# Problem: First Bad Version
# Language: python3
# Runtime: 28 ms
# Memory: 13 MB

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        
        while left != right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return mid if isBadVersion(mid) else mid + 1
    