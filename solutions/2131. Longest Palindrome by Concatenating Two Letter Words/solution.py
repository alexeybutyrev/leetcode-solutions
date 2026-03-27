# Problem: Longest Palindrome by Concatenating Two Letter Words
# Language: python3
# Runtime: 1666 ms
# Memory: 38.6 MB

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        c = Counter(words)
        ans = 0

        for w in c:
            if w == w[::-1]:
                d,m = divmod(c[w],2)
                ans += 4 * d
                
                c[w] = m
        
        dub = False
        for w in c:
            if w != w[::-1] and w[::-1] in c:
                ans += 4 * min(c[w], c[w[::-1]])

                c[w] = c[w[::-1]] = 0

        for w in c:
            if w == w[::-1] and c[w]:
                ans += 2
                break
        
                
            
        return ans
                    
                    
                    