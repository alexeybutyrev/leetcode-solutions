# Problem: Count the Number of K-Big Indices
# Language: python3
# Runtime: 2175 ms
# Memory: 35.4 MB

class Solution:
    def kBigIndices(self, A: List[int], k: int) -> int:
        def count(A,r = True):
            BIT = Counter()
            M = max(A) + 1
            def count(x):
                s = 0
                while x:
                    s += BIT[x]
                    x -= x & (-x)
                return s
            
            def update(x):
                while x < M+1:
                    BIT[x] += 1
                    x += x & (-x)

            ans = set()
            for i,a in enumerate(A):
                c = count(a-1)
                
                if c >= k:
                    if r:
                        ans.add(i)
                    else:
                        ans.add(N-1-i)
                update(a)
            return ans
        
        N = len(A)
        a1 = count(A)
        a2 = count(A[::-1], False)
        return len(a1&a2) 