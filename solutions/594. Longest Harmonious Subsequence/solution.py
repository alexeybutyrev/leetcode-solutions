# Problem: Longest Harmonious Subsequence
# Language: python3
# Runtime: 400 ms
# Memory: 17 MB

class Solution:
    def findLHS(self, A: List[int]) -> int:
        
        c = Counter(A)
        
        B = [(k,v) for k,v in c.items()]
        B.sort()
        
        ans = 0
        l = 0
        for i in range(1,len(B)):
            if B[i][0] - B[i-1][0] == 1:
                l = B[i][1] + B[i-1][1]
                ans = max(l, ans)
        
        
        return ans