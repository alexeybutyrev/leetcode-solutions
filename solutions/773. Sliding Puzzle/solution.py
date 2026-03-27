# Problem: Sliding Puzzle
# Language: python3
# Runtime: 15 ms
# Memory: 17 MB

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        T = tuple(tuple(x) for x in board)
        seen = {T}
        q = deque([T])
        
        TARGET = tuple([(1,2,3),(4,5,0)])
        
        def gen(T):
            for i in range(2):
                p = False
                for j in range(3):
                    if T[i][j] == 0:
                        p = not p
                        break
                if p:
                    break
            L = [list(x) for x in T]
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < 2 and 0 <= y < 3:
                    a,b = L[x][y],L[i][j]
                    L[x][y], L[i][j] = b,a
                    yield tuple(tuple(x) for x in L)
                    L[x][y],L[i][j] = a,b
        
        
        ans = 0
        while q:
            L = len(q)
            for _ in range(L):
                t = q.popleft()
                
                if t == TARGET:
                    return ans
                
                for n in gen(t):
                    if n not in seen:
                        seen.add(n)
                        q.append(n)
                
            ans += 1
                
            
        return -1