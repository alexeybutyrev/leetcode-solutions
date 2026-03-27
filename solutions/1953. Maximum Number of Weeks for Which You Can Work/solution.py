# Problem: Maximum Number of Weeks for Which You Can Work
# Language: python3
# Runtime: 752 ms
# Memory: 26.7 MB

class Solution:
    def numberOfWeeks(self, H: List[int]) -> int:
        N = len(H)
        mx = max(H)
        sm = sum(H)
        if sm - mx >= mx:
            return sm
        return 2 *(sm - mx) + 1
            
        
        
            