# Problem: Robot Bounded In Circle
# Language: python3
# Runtime: 24 ms
# Memory: 14 MB

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0,0]
        direction = (0,1)
        point = [0,0]
        
        rotation_left = {(0,1):(-1,0),
                         (-1,0):(0,-1),
                         (0,-1):(1,0),
                         (1,0):(0,1)}
        
        rotation_right = {(0,1):(1,0),
                         (1,0):(0,-1),
                         (0,-1):(-1,0),
                         (-1,0):(0,1)}
        
        for _ in range(4):
            for i in instructions:
                if i == 'G':
                    point[0] += direction[0]
                    point[1] += direction[1]
                elif i == "L":
                    direction = rotation_left[direction]
                else:
                    direction = rotation_right[direction]
            if point == start:
                return True
            
        return False