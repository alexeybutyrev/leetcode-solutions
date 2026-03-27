# Problem: Find Words That Can Be Formed by Characters
# Language: python3
# Runtime: 153 ms
# Memory: 16.9 MB

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        ans = 0
        for w in words:
            cw = Counter(w)
            for k,v in cw.items():
                if c[k] < v:
                    break
            else:
                ans += len(w)
        return ans