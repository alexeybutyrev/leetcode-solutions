# Problem: K Highest Ranked Items Within a Price Range
# Language: python3
# Runtime: 7270 ms
# Memory: 57.9 MB

class Solution:
    def highestRankedKItems(self, A: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        
        N, M = len(A),len(A[0])
        h = []
        heappush(h,(0,A[start[0]][start[1]],start[0],start[1]))
        
        ans = []
        seen = {(start[0],start[1])}
        
        while h:
            d,p,i,j = heappop(h)
            if pricing[0] <= p <= pricing[1]:
                heappush(ans, (d,p,i,j))            
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                x = i + dx
                y = j + dy
                if x < N and x >=0 and y < M and y >= 0 and A[x][y] and (x,y) not in seen:
                    seen.add((x,y))
                    heappush(h,(d+1,A[x][y],x,y))
        res = []
        while ans and len(res) < k:
            d,p,i,j = heappop(ans)
            res.append([i,j])
        return res 
        
        