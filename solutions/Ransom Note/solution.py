# Problem: Ransom Note
# Language: python3
# Runtime: 52 ms
# Memory: 14 MB

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        
        for r in rc:
            if r in mc and rc[r] <= mc[r]:
                continue
            else:
                return False
        return True