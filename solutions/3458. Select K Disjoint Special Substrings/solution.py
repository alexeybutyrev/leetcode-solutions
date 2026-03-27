# Problem: Select K Disjoint Special Substrings
# Language: python3
# Runtime: 335 ms
# Memory: 18.2 MB

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:

        first = {}
        last  = {}
        c = Counter()
        for i, x in enumerate(s):
            first.setdefault(x,i)
            last[x] = i
            c[x] += 1
        
        A = []
        for x,i in first.items():
            for y,j in last.items():
                if i <= j:
                    cnt = 0
                    for XXX in c:
                        if i <= first[XXX] <= last[XXX] <= j:
                            cnt += c[XXX]
                    if cnt == j -i + 1 and cnt < len(s):
                        A.append([i,j])
        A.sort(key = lambda s: s[1] - s[0])
        res = []
        for i,j in A:
            if all(y < i or j < x for x,y in res):
                res.append([i,j])
        return len(res) >= k