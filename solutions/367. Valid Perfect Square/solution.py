# Problem: Valid Perfect Square
# Language: python
# Runtime: 16 ms
# Memory: 11.8 MB

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if 1 == num: return True
        left, right = 0, num -1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                right = mid
            else:
                left = mid
                
        return False