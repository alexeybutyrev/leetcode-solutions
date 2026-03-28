# Problem: Palindrome Partitioning IV
# Language: python3
# Runtime: 9532 ms
# Memory: 14.4 MB

import re
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        is_pali = lambda x: x == x[::-1]

        N = len(s)
        
        for i in range(N):
            if is_pali(s[0:i+1]):
                for j in range(i+1,N):
                    if is_pali(s[i+1:j+1]) & is_pali(s[j+1:]):
                        return True
        
        return False