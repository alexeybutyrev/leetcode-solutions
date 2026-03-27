# Problem: Minimum Number of Swaps to Make the String Balanced
# Language: python3
# Runtime: 160 ms
# Memory: 28 MB

class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        nl = 0
        nr = 0
        for l in s:
            if l == "[":
                nl += 1
            else:
                if not nl:
                    nr += 1
                else:
                    nl -= 1
        
            
        return ceil(nl/2)
    