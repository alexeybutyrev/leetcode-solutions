# Problem: K Divisible Elements Subarrays
# Language: python3
# Runtime: 2027 ms
# Memory: 28.9 MB

class Solution:
    def countDistinct(self, A: List[int], k: int, p: int) -> int:

#3
#14
        N = len(A)
        ans = N * (N + 1) // 2
        s = set()
        for i in range(N):
            c = Counter()
            c[A[i]] += 1
            s.add(tuple(A[i:i+1]))
            for j in range(i+1,N):
                c[A[j]] += 1
                count = 0
                for key,v in c.items():
                    if key % p == 0:
                        count += v
                
                if count <= k:
                    s.add(tuple(A[i:j+1]))
        
        return len(s)