# Problem: Robot Collisions
# Language: python3
# Runtime: 1047 ms
# Memory: 47.9 MB

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        A = []
        for i,(p,h,d) in enumerate(zip(positions, healths, directions)):
            A.append((p,h,d,i))
        A.sort()
        
        stack = []
        for p,h,d,i in A:
            if stack and stack[-1][-1] == 'R' and d == 'L':
                while stack and stack[-1][-1] == 'R':
                    if h == stack[-1][1]:
                        stack.pop()
                        h = 0
                        break
                    elif h < stack[-1][1]:
                        stack[-1][1] -= 1
                        h = 0
                        break
                    else:
                        h -= 1
                        stack.pop()
                if h:
                    stack.append([i,h,d])
            else:
                stack.append([i,h,d])
        
        stack.sort()
        
        return [h for _,h,_ in stack]
    
                    
                
                