# Problem: Minimum Moves to Move a Box to Their Target Location
# Language: python3
# Runtime: 599 ms
# Memory: 31.2 MB

class Solution:
    def minPushBox(self, A: List[List[str]]) -> int:
        N, M = len(A), len(A[0])
        valid = set()
        for i in range(N):
            for j in range(M):
                if A[i][j] == ".":
                    valid.add((i,j))
                elif A[i][j] == "S":
                    player = (i,j)
                    valid.add((i,j))
                elif A[i][j] == "B":
                    box = (i,j)
                    valid.add((i,j))
                elif A[i][j] == "T":
                    target = (i,j)
                    valid.add((i,j))
        
        h = []
        heappush(h,(0, box[0], box[1], player[0], player[1]))
        seen = defaultdict(lambda : inf)
        while h:
            d,x,y,i,j = heappop(h)
            if (x,y) not in valid or (i,j) not in valid: continue
            if (x,y) == target: 
                return d
            
            # move person
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                xx = i + dx
                yy = j + dy
                if seen[(x,y,xx,yy)] > d and (x,y) != (xx,yy):
                    seen[(x,y,xx,yy)] = d
                    heappush(h,(d,x,y,xx,yy))
            
            
            if x == i + 1 and y == j and seen[(x+1,y,i+1,j)] > d + 1:
                seen[(x+1,y,i+1,j)] = d + 1
                heappush(h,(d+1,x+1,y,i+1,j))
            
            if x == i - 1 and y == j and seen[(x-1,y,i-1,j)] > d + 1:
                seen[(x-1,y,i-1,j)] = d + 1
                heappush(h,(d+1,x-1,y,i-1,j))
            
            if x == i and y == j+1 and  seen[(x,y+1,i,j+1)] > d + 1:
                seen[(x,y+1,i,j+1)] = d + 1
                heappush(h,(d+1,x,y+1,i,j+1))
                
            if x == i and y == j-1 and seen[(x,y-1,i,j-1)] > d + 1:
                seen[(x,y-1,i,j-1)] = d + 1
                heappush(h,(d+1,x,y-1,i,j-1))
            
            
        return -1
        
        self.ans = inf
        @cache
        def dp(x,y,i,j,c):
            
            if (x,y) == target:
                self.ans = min(self.ans, c)
                return c
            if (x,y) == (i,j) or (x,y) not in valid or (i,j) not in valid or seen[(x,y,i,j)] <= c:
                return inf
            
            seen[(x,y,i,j)] = c
            
            # move person
            p1 = dp(x,y,i,j+1,c)
            p2 = dp(x,y,i,j-1,c)
            p3 = dp(x,y,i-1,j,c)
            p4 = dp(x,y,i+1,j,c)
            
            ans = min(p1,p2,p3,p4)
            
            # move box and person
            if x == i + 1 and y == j:
                #print('!', x,y,i,j)
                ans = min(ans, dp(x+1,y,i+1,j,c+1))
            if x == i - 1 and y == j:
                ans = min(ans, dp(x-1,y,i-1,j,c+1))
            
            if x == i and y == j+1:
                ans = min(ans, dp(x,y+1,i,j+1,c+1))
            if x == i and y == j-1:
                ans = min(ans, dp(x,y-1,i,j-1,c+1))
            return ans
        ans = dp(box[0],box[1],player[0],player[1],0)
        return -1 if ans == inf else ans
            
            