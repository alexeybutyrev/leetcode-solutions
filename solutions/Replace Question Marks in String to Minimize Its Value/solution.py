# Problem: Replace Question Marks in String to Minimize Its Value
# Language: python3
# Runtime: 292 ms
# Memory: 18.7 MB


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        h = []
        c = Counter(s)
        for x in ascii_lowercase:
            heappush(h, (c[x], x))
        
        q = []
        for x in s:
            if x == '?':
                count, y = heappop(h)
                q.append(y)
                heappush(h, (count+1,y))
        
        q.sort()
        q = deque(q)
        
        
        
        ans = []
        
        for x in s:
            if x == "?":
                ans.append(q.popleft())
            else:
                ans.append(x)
                           
            
        
        return "".join(ans)