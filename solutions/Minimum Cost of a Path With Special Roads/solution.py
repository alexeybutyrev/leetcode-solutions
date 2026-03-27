# Problem: Minimum Cost of a Path With Special Roads
# Language: python3
# Runtime: 2170 ms
# Memory: 63.4 MB

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        TX,TY = target
        x,y = start
        seen = set()
        seen.add((x,y))
        seen.add((TX,TY))
        
        graph = defaultdict(set)
        dist = defaultdict(lambda: inf)
        for x1,y1,x2,y2,c in specialRoads:
            dist[(x1,y1,x2,y2)] = min(dist[(x1,y1,x2,y2)],c, abs(x2-x1) + abs(y2-y1))
            graph[(x1,y1)].add((x2,y2))
            
            graph[(x2,y2)].add((x1,y1))
            dist[(x2,y2,x1,y1)] = min(dist[(x2,y2,x1,y1)],abs(x2-x1) + abs(y2-y1))
            
            dist[(x2,y2,TX,TY)] = min(dist[(x2,y2,TX,TY)],abs(x2-TX) + abs(y2-TY))
            graph[(x2,y2)].add((TX,TY))
            
            dist[(x,y,x1,y1)] = min(dist[(x,y,x1,y1)], abs(x-x1) + abs(y-y1))
            graph[(x,y)].add((x1,y1))
            
            seen.add((x1,y1))
            seen.add((x2,y2))
        
        N = len(seen)
        seen = list(seen)
        
        for i in range(N):
            for j in range(i+1,N):
                x1,y1 = seen[i]
                x2,y2 = seen[j]
                graph[(x1,y1)].add((x2,y2))
                graph[(x2,y2)].add((x1,y1))
                if dist[(x1,y1,x2,y2)] > abs(x1-x2) + abs(y1-y2):
                    dist[(x1,y1,x2,y2)] = abs(x1-x2) + abs(y1-y2)
                
                if dist[(x2,y2,x1,y1)] > abs(x1-x2) + abs(y1-y2):
                    dist[(x2,y2,x1,y1)] = abs(x1-x2) + abs(y1-y2)
        
        h = []
        
        dist[(x,y,x,y)] = 0
        heappush(h,(0, x,y,x,y))
        
        dist[(x,y,TX,TY)] = min(dist[(x,y,TX,TY)], abs(TX-x) + abs(TY-y))
        heappush(h,(dist[(x,y,TX,TY)], x,y,TX,TY))
        
        for a,b in graph[(x,y)]:
            heappush(h, (dist[(x,y,a,b)],x,y,a,b))
        while h:
            d,x1,y1,x2,y2 = heappop(h)
            if d > dist[(x1,y1,x2,y2)]: continue
            # if x2==TX and y2==TY: return d
            for x3,y3 in graph[(x2,y2)]:
                if dist[(x1,y1,x3,y3)] > dist[(x2,y2,x3,y3)] + d:
                    dist[(x1,y1,x3,y3)] = dist[(x2,y2,x3,y3)] + d
                    heappush(h, (dist[(x1,y1,x3,y3)] ,x1 ,y1 ,x3, y3))
        
        return dist[(x,y,TX,TY)]
        