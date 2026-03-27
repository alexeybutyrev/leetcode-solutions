# Problem: Mean of Array After Removing Some Elements
# Language: python3
# Runtime: 92 ms
# Memory: 14.4 MB

from heapq import *
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        k = n  // 20
        s = 0
        for i in range(k, n -k):
            s += arr[i]
        return s / (n - 2 *k)
        
            