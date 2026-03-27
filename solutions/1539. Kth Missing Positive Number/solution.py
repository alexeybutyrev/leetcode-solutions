# Problem: Kth Missing Positive Number
# Language: python3
# Runtime: 43 ms
# Memory: 14.1 MB

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        s = set(arr)
        for x in range(1,10001):
            if x not in s:
                k-=1
            if k == 0:
                return x
        return x
        