# Problem: Minimum Number of Moves to Make Palindrome
# Language: python3
# Runtime: 1017 ms
# Memory: 13.9 MB

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        i,j = 0, len(s) - 1
        ans = 0
        s = list(s)
        while i < j:
            if s[i] != s[j]:
                k = j
                while k > i and s[i] != s[k]:
                    k-=1
                if i == k:
                    s[i],s[i+1] = s[i+1], s[i]
                    ans += 1
                else:
                    
                    while k < j:
                        s[k],s[k+1] = s[k+1], s[k]
                        k += 1
                        ans += 1
                    i += 1
                    j -= 1
                    
                
            else:
                i += 1
                j -= 1
        return ans