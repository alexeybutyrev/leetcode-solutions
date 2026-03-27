# Problem: Minimum Jumps to Reach Home
# Language: python3
# Runtime: 147 ms
# Memory: 15.5 MB

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque()
        forbidden = set(forbidden)
        seen = set()
        q.append((0, False, 0))
        #print(q[0])
        #cord, visited, backed, count = q.popleft()
        
        mx = 8000
        while q:
            l = len(q)
            for _ in range(l):
                cord,  backed, count = q.popleft()
                if cord == x:
                    return count
                    
                if not backed and cord - b > 0 and (cord - b,backed) not in seen and cord - b not in forbidden:
                    q.append((cord-b,True, count+1))
                    seen.add((cord-b,True))
                
                if (cord + a,backed) not in seen and cord + a not in forbidden and cord + a < mx:
                    q.append((cord+a,False,count+1))
                    seen.add((cord+a,False))
            
        
        return -1