# Problem: Odd Even Jump
# Language: python3
# Runtime: 512 ms
# Memory: 39.5 MB

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        
        # find odd jumps
        B = [ (a, i) for i,a in enumerate(A)]
        B.sort()
        odd_dp = defaultdict(lambda : -1)
        
        for i in range(N):
            for j in range(i+1, N):
                if B[j][1] > B[i][1]:
                    odd_dp[B[i][1]] = B[j][1]
                    break
        
        
        # find even jumps
        even_dp = defaultdict(lambda : -1)
        B.sort(key = lambda x: (-x[0], x[1]) )
        
        for i in range(N-1):
            for j in range(i+1, N):
                if B[j][1] > B[i][1]:
                    even_dp[B[i][1]] = B[j][1]
                    break
        

        # check if we can move
        @lru_cache(None)
        def walk(i, o):
            if i == N - 1:
                return 1
            
            if (o and odd_dp[i] >= 0):
                return walk(odd_dp[i], not o)
            elif (not o and even_dp[i] >= 0):
                return walk(even_dp[i], not o)
            else:
                return 0
        
        count = 0
        for i in range(N):
            count += walk(i, True)

        
        return count 
        
            