# Problem: Most Frequent Even Element
# Language: python3
# Runtime: 310 ms
# Memory: 14.5 MB

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        A = [(-v,k) for k,v in c.items() if k % 2 == 0]
        A.sort()
        if not A:
            return -1
        
        return A[0][1]
    