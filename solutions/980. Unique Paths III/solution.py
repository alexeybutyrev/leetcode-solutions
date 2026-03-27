# Problem: Unique Paths III
# Language: python3
# Runtime: 113 ms
# Memory: 25.2 MB

class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        N = len(A)
        M = len(A[0])
        count = 0
        bricks = set()
        for i in range(N):
            for j in range(M):
                if A[i][j] == 0:
                    count += 1
                elif A[i][j] == 1:
                    start = (i,j)
                elif A[i][j]== -1:
                    bricks.add((i,j))
                else:
                    end = (i,j)
        
        paths = {tuple([start])}
        q = [(start[0],start[1],tuple([start]),{start})]
        
        ans = 0
        for i,j,path,seen in q:
            if (i,j) == end:
                if len(path) == count+2:
                    ans+=1
                continue
            p = list(path)
            for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
                x = i + dx
                y = j + dy
                new_p = tuple(p + [(x,y)])
                if (x >= 0 and x < N and y >= 0 and y < M 
                    and (x,y) not in seen and (x,y) not in bricks and new_p not in paths
                   ):
                    paths.add(tuple(p + [(x,y)]))
                    q.append((x,y,new_p,seen |{(x,y)}))
        
        return ans