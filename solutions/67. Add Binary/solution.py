# Problem: Add Binary
# Language: python
# Runtime: 12 ms
# Memory: 11.8 MB

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]