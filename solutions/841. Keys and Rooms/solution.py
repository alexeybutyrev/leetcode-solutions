# Problem: Keys and Rooms
# Language: python3
# Runtime: 52 ms
# Memory: 14.9 MB

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        N = len(rooms)
        
        q = deque()
        q.append(0)
        
        
        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                for k in rooms[node]:
                    if k not in visited:
                        q.append(k)
                        visited.add(k)
                    
            
            if len(visited) == N:
                return True
        
        return False