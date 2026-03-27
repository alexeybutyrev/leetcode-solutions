# Problem: Longest Substring Of All Vowels in Order
# Language: python3
# Runtime: 1832 ms
# Memory: 20.2 MB

class Solution:
    def longestBeautifulSubstring(self, S: str) -> int:
        N = len(S)
        c = Counter()
        i = 0
        j = 1
        c[S[0]] += 1
        ans = 0
        while i < N and j < N:
            if S[j] >= S[j-1]:
                c[S[j]] += 1
                
            else:
                for k in range(i,j):
                    c[S[k]] -= 1
                    if not c[S[k]]:
                        del c[S[k]]
                i = j
                c[S[i]] += 1
            j+=1
            if len(c) == 5:
                ans = max(ans, j - i)
        return ans