# Problem: The Maze III
# Language: python3
# Runtime: 7 ms
# Memory: 19.5 MB

class Solution:
    def findShortestWay(self, A: List[List[int]], ball: List[int], hole: List[int]) -> str:
        h = []
        N, M = len(A), len(A[0])
        heappush(h,(0,'',ball[0],ball[1]))
        
        dist = defaultdict(lambda :inf)
        def walk(i,j):
            for (dx,dy,l) in [(-1,0,'u'),(1,0,'d'),(0,-1,'l'),(0,1,'r')]:
                x = i
                y = j
                dd = 0
                while 0 <= x + dx < N  and 0 <= y + dy < M and A[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    dd += 1
                    if [x,y] == hole:
                        break
                yield x,y, l, dd
        
        seen = set()
        while h:
            #print(h)
            d,s,i,j = heappop(h)
            if (i,j) in seen: continue
            if [i,j] == hole: return s
            seen.add((i,j))
            for x,y,l,dd in walk(i,j):
                heappush(h, (d + dd, s + l, x,y))
                
                
            
        return "impossible"