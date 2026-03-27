# Problem: Nested List Weight Sum II
# Language: python3
# Runtime: 0 ms
# Memory: 18.2 MB

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, L: List[NestedInteger]) -> int:
        ans = 0 
        maxDepth = 0
        L1 = L[:]
        # BFS
        q = deque([L])
        while q:
            L = len(q)
            maxDepth += 1
            for _ in range(L):
                l = q.popleft()
                for x in l:
                    if x.getList():
                        q.append(x.getList())

        
        q = []
        for l in L1:
            q.append((maxDepth,l))

        # DFS
        ans = 0
        for m,l in q:
            
            if l.getInteger() is None:
                for le in l.getList():
                    q.append((m - 1, le))
            else:
                ans += m * l.getInteger()
            
        return ans
