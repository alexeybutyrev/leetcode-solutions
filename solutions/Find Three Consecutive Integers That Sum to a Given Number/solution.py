# Problem: Find Three Consecutive Integers That Sum to a Given Number
# Language: python
# Runtime: 23 ms
# Memory: 13.4 MB

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 == 0:
            c = num // 3 -1
            return [c,c+1,c+2]
        return []