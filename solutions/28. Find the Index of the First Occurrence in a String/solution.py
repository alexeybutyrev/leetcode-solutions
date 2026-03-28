# Problem: Find the Index of the First Occurrence in a String
# Language: python
# Runtime: 16 ms
# Memory: 12.1 MB

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)