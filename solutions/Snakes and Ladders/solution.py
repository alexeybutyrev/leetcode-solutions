# Problem: Snakes and Ladders
# Language: python3
# Runtime: 144 ms
# Memory: 13.9 MB

class Solution:
    def snakesAndLadders(self, A: List[List[int]]) -> int:
        N = len(A)
        def ind2cord(i):
            x = (i-1) // N
            y = i - (x) * N-1
            if x & 1:
                y = N - y -1
            return (x,y)
        A = A[::-1]
        
        q = deque([1])
        ans = 0
        seen = {1}
        while q:
            #print(q)
            L = len(q)
            for _ in range(L):
                x = q.popleft()
                if x == N*N: return ans
                for d in range(1,7):
                    y = x + d
                    if y > N*N: continue
                    i,j = ind2cord(y)
                    y = y if A[i][j] == -1 else A[i][j]
                    if y not in seen:
                        seen.add(y)
                        q.append(y)
                    
            ans+=1
        return -1
         