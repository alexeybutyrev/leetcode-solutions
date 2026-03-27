# Problem: High-Access Employees
# Language: python3
# Runtime: 190 ms
# Memory: 16.4 MB

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for a, t in access_times:
            hh = int(t[:2])
            mm = int(t[2:])
            T = hh*60 + mm
            d[a].append(T)
        
        ans = []
        for x in d:
            d[x].sort()
            for i in range(len(d[x])):
                if i>1 and d[x][i] - d[x][i-2] < 60:
                    ans.append(x)
                    break
        return ans
        
        
        
        