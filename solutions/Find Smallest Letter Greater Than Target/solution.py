# Problem: Find Smallest Letter Greater Than Target
# Language: python
# Runtime: 84 ms
# Memory: 13.7 MB

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]