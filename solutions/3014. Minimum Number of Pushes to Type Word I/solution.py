# Problem: Minimum Number of Pushes to Type Word I
# Language: python3
# Runtime: 31 ms
# Memory: 16.6 MB

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        N = 8
        d = defaultdict(list)
        
        A = [(-v,k) for k,v in c.items()]
        A.sort()
        
        curr = 0
        for _,k in A:
            curr %= N
            d[curr].append(k)
            curr += 1
        
        hm = {}
        for k,l in d.items():
            for i,x in enumerate(l):
                hm[x] = i + 1
        
        ans = 0
        for x in word:
            ans += hm[x]
        return ans