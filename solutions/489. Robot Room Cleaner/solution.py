# Problem: Robot Room Cleaner
# Language: python3
# Runtime: 72 ms
# Memory: 15.6 MB

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def turn_back(root):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        directions = [(-1,0), (0,1),(1,0), (0,-1)]
        
        seen = set()
        
        def backtrack(point, d):
            seen.add(point)
            robot.clean()
            for i in range(4):
                d0 = (d + i) % 4
                x = point[0] + directions[d0][0]
                y = point[1] + directions[d0][1]
                if (x,y) not in seen and robot.move():
                    backtrack((x,y),d0)
                    turn_back(robot)
                robot.turnRight()

            
                 
                
        
        backtrack((0,0), 0)
        
        