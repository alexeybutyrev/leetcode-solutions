# Problem: Count Sorted Vowel Strings
# Language: python3
# Runtime: 9329 ms
# Memory: 90.4 MB

class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = ['a', 'e', 'i', 'o', 'u']
        v = ['a', 'e', 'i', 'o', 'u']
        for _ in range(n-1):
            ans2 = []
            for a in ans:
                for s in v:
                    if s >= a[-1]:
                        ans2.append(a + s)
            ans = ans2[:]
        
        return len(ans)
                