# Problem: Count of Substrings Containing Every Vowel and K Consonants I
# Language: python3
# Runtime: 9429 ms
# Memory: 16.6 MB

class Solution:
    def countOfSubstrings(self, S: str, k: int) -> int:
        N = len(S)
        ans = 0
        for i in range(N):
            for j in range(i+1,N+1):
                s0 = S[i:j]
                c = Counter(s0)
                seen = False
                for x in ['a', 'e', 'i', 'o', 'u']:
                    if x in c:
                        del c[x]
                        seen = True
                    else:
                        seen = False
                        break
                s = sum(c.values())
                if s == k and seen:
                    ans += 1
        return ans