# Problem: Cells in a Range on an Excel Sheet
# Language: python3
# Runtime: 47 ms
# Memory: 14 MB

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        L1,L2 = s[0],s[3]
        R1,R2 = int(s[1]), int(s[4])
        
        ans = []
        for i in range(ord(L1), ord(L2) + 1):
            for j in range(R1,R2+1):
                ans.append(chr(i) + str(j))
        return ans