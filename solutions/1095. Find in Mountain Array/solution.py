# Problem: Find in Mountain Array
# Language: python3
# Runtime: 32 ms
# Memory: 14.9 MB

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        left, right = 0, mountain_arr.length() - 1
        while left != right:
            mid = (left + right) // 2
            vl = mountain_arr.get(mid)
            vr = mountain_arr.get(mid+1)
            
            if vl > vr:
                right = mid
            else:
                left = mid + 1
                

        i, j = 0, left
        while i <= j:
            mid = i + (j - i) // 2
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            if v < target:
                i = mid + 1
            else:
                j = mid - 1
        
        
        i, j = left+1, mountain_arr.length() - 1
        if mountain_arr.get(j) == target:
            return j
        while i <= j:
            mid = i + (j - i) // 2
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            if v < target:
                i = mid + 1
            else:
                j = mid - 1
        
        
        return -1

        
        
