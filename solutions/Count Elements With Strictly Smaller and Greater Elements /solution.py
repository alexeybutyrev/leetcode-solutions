# Problem: Count Elements With Strictly Smaller and Greater Elements 
# Language: python3
# Runtime: 40 ms
# Memory: 14.1 MB

class Solution:
    def countElements(self, A: List[int]) -> int:
        
        mn = min(A)
        mx = max(A)
        return sum(1 for a in A if a not in {mn,mx})