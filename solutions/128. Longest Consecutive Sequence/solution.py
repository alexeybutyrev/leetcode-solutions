# Problem: Longest Consecutive Sequence
# Language: python3
# Runtime: 983 ms
# Memory: 47.1 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        S = set(nums)
        
        for n in S:
            union(n,n)
            if n+1 in S:
                union(n+1,n)
        
        c = Counter()
        for n in S:
            c[find(n)]  +=1
        
        return max(c.values())