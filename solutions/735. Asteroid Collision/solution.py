# Problem: Asteroid Collision
# Language: python3
# Runtime: 102 ms
# Memory: 17.4 MB

class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stack = []
        
        for x in A:
            if stack:
                while stack and stack[-1] > 0 and x < 0:
                    y = stack.pop()
                    if -x == y:
                        break
                    elif abs(x) < y:
                        stack.append(y)
                        break
                else:
                    stack.append(x)
            else:
                stack.append(x)
                
        
        return stack