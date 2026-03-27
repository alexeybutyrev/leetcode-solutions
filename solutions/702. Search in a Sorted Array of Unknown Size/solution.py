# Problem: Search in a Sorted Array of Unknown Size
# Language: python
# Runtime: 28 ms
# Memory: 12.4 MB

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        ind = 1
        v = reader.get(ind)
        print(v, ind)
        while v < target and v != 2147483647:
            if v == 2147483647:
                ind = ind / 2 + ind //4
            else:
                ind = ind * 2
            v = reader.get(ind)
            
        print(v, ind)
        if v == target:
            return ind
        
    
        right = ind - 1
        left = ind // 2
        
        while left + 1 < right:
            mid = (left + right) // 2
            v = reader.get(mid)
            if v < target:
                left = mid
            elif v > target:
                right = mid
            else:
                return mid
            
        return -1
    
        