# Problem: Water and Jug Problem
# Language: python3
# Runtime: 3229 ms
# Memory: 91.3 MB

class Solution:
    def canMeasureWater(self, A: int, B: int, target: int) -> bool:
        q = [(0,0)]
        seen = {(0,0)}
        for x,y in q:
            #print(q)
            if x == target or y == target or x + y == target:
                return True
            # fill x
            if (A,y) not in seen:
                seen.add((A,y))
                q.append((A,y))
            
            # fill y
            if (x,B) not in seen:
                seen.add((x,B))
                q.append((x,B))
            
            # pour x
            if (0,y) not in seen:
                seen.add((0,y))
                q.append((0,y))
            
            # pour y
            if (x,0) not in seen:
                seen.add((x,0))
                q.append((x,0))
            
                
            dx = A - x
            dy = B - y
            # move x to y
            if x <= dy:
                state = (0,y + x)
                if state not in seen:
                    seen.add(state)
                    q.append(state)
            else:
                state = (x-dy,B)
                if state not in seen:
                    seen.add(state)
                    q.append(state)
                    
            if y <= dx:
                state = (x+y,0)
                if state not in seen:
                    seen.add(state)
                    q.append(state)
            else:
                state = (A,y-dx)
                if state not in seen:
                    seen.add(state)
                    q.append(state)
            
            
        return False
            