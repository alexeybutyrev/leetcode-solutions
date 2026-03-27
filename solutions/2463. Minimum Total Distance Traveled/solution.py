# Problem: Minimum Total Distance Traveled
# Language: python3
# Runtime: 6748 ms
# Memory: 448.2 MB

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        A = []
        robot.sort()
        factory.sort()
        NR = len(robot)
        NF = len(factory)

        @cache
        def dp(i,j,l):
            if j == NF or factory[j][1] < l:
                return inf
            
            if i == NR: return 0
            
            s1 = dp(i,j+1,0)
            s2 = abs(robot[i] - factory[j][0]) + dp(i+1,j,l+1)
            return min(s1,s2)
        return dp(0,0,0)
    