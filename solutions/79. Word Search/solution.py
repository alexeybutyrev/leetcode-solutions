# Problem: Word Search
# Language: python3
# Runtime: 2815 ms
# Memory: 358.9 MB

class Solution:
    def exist(self, A: List[List[str]], word: str) -> bool:
        N, M = len(A), len(A[0])
        q = deque()
        c1 = Counter(word)
        c2 = Counter()
        for i in range(N):
            for j in range(M):
                c2[A[i][j]] += 1
                if A[i][j] == word[0]:
                    q.append((i,j,{(i,j)}))
        for k in c1:
            if c1[k] > c2[k]:
                return False
        
        for wi in range(1,len(word)):
            if not q: return False
            L = len(q)
            for _ in range(L):
                i,j,seen = q.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < N and 0 <= y < M and (x,y) not in seen and A[x][y] == word[wi]:
                        q.append((x,y, seen | {(x,y)}))
                       
        return True if q else False