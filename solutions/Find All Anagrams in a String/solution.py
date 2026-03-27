# Problem: Find All Anagrams in a String
# Language: python3
# Runtime: 160 ms
# Memory: 14.9 MB

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp = Counter(p)
        NP = len(p)
        ans = []
        for i in range(len(s)-NP+1):
            if i == 0:
                cs = Counter(s[i:i+NP])
            else:
                cs[s[i+NP-1]] += 1
                cs[s[i-1]] -= 1
                if not cs[s[i-1]]:
                    del cs[s[i-1]]
            if cs == cp:
                ans.append(i)
        return ans
    