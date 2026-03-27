# Problem: Check If Array Pairs Are Divisible by k
# Language: python3
# Runtime: 571 ms
# Memory: 30.6 MB

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        N = len(arr) // 2
        c = Counter()
        count = 0
        for x in arr:
            key = k - (x%k)
            if key in c and c[key]:
                c[key] -= 1
                count += 1
            else:
                c[x % k or k] += 1
        
        return N == count