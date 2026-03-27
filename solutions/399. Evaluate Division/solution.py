# Problem: Evaluate Division
# Language: python3
# Runtime: 51 ms
# Memory: 16.5 MB

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vals = Counter()
        graph = defaultdict(list)
        for i,(u,v) in enumerate(equations):
            graph[u].append(v)
            graph[v].append(u)
            vals[(u,v)] = values[i]
            vals[(v,u)] = 1.0 / values[i]
            vals[(u,u)] = 1.0
            vals[(v,v)] = 1.0
        
        
        ans = []
        for u,v in queries:
            if u == v and (u,v) not in vals:
                ans.append(-1)
                continue
            
            if (u,v) in vals:
                ans.append(vals[(u,v)])
            else:
                
                q = [(u,u,1)]
                seen = {(u,u)}
                for f, t, m in q:
                    vals[(u,t)] = m
                    vals[(t,u)] = 1.0 / m
                    if t == v:
                        ans.append(m)
                        break
                    for node in graph[t]:
                        if (t,node) not in seen:
                            seen.add((t,node))
                            q.append((t,node,m*vals[(t,node)]))
                    
                        
                else:
                    ans.append(-1)
                        
            
        return ans
        
        