# Problem: Poor Pigs
# Language: python
# Runtime: 21 ms
# Memory: 13.3 MB

class Solution(object):
    def poorPigs(self, B, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        nt = minutesToTest // minutesToDie + 1
        return int(ceil(log(B)/log(nt)))