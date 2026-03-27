# Problem: Next Closest Time
# Language: python3
# Runtime: 40 ms
# Memory: 14.2 MB

class Solution:
    def nextClosestTime(self, time: str) -> str:
        d = set()
        for l in time:
            if l.isdigit():
                d.add(l)
        
        def diff(t1,t2):
            c = t1.split(":")[0].lstrip("0")
            h1 = int(c) if c else 0
            c = t2.split(":")[0].lstrip("0")
            h2 = int(c) if c else 0
            
            c = t1.split(":")[1].lstrip("0")
            m1 = int(c) if c else 0
            
            c = t2.split(":")[1].lstrip("0")
            m2 = int(c) if c else 0
            
            return (h2 - h1) * 60 + m2 - m1 
        
        def is_legal(t):
            t = [t[0], t[1], t[3], t[4]]
            
            if t[0] not in ['0','1','2']:
                return False
            
            if int(t[2]) >= 6:
                return False
            
            
            if t[0] == '2' and t[1] not in ['0','2','1','3']:
                return False
            
            return True

        q = deque([""])
        times = set()
        while q:
            l = len(q)
            for _ in range(l):
                t = q.popleft()
                if len(t) == 5:
                    if is_legal(t):
                        times.add(t)
                    continue

                if len(t) == 2:
                    t+=":"

                for l in d:
                    q.append(t+l)
        
        d = inf
        ans = ""
        for t in times:
            delta = diff( time, t)
            if delta > 0 and delta < d:
                ans = t
                d = delta
        
        if not ans:
            d = 0
            for t in times:
                delta = diff(time, t)
                if delta < 0 and abs(delta) > d:
                    ans = t
                    d = abs(delta)

                
        if not ans:
            return time
        return ans
        
            