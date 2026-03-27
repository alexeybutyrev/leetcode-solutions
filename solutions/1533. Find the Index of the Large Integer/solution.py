# Problem: Find the Index of the Large Integer
# Language: python3
# Runtime: 276 ms
# Memory: 53.1 MB

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        N= reader.length()
        lo, hi = 0, N - 1
        
        while lo < hi:
            mid = lo + hi >> 1
            
            if (hi - lo + 1) % 2 == 0 :
                x = reader.compareSub(lo, mid, mid + 1, hi)
            else:
                x = reader.compareSub(lo, mid, mid, hi)
            
            if x < 0:
                lo = mid + 1
            else:
                hi = mid
        return lo