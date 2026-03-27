# Problem: Maximum Vacation Days
# Language: python3
# Runtime: 3697 ms
# Memory: 21.6 MB

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(flights)
        
        for i in range(N):
            for j in range(N):
                if flights[i][j]:
                    graph[i].append(j)
        
        K = len(days[0])
            
        @cache
        def dp(week,i):
            if week == K:
                return 0
            
            ans = days[i][week] + dp(week+1,i)
            for j in graph[i]:
                ans = max(ans, days[j][week] + dp(week+1,j))
            return ans
            
        return dp(0,0)