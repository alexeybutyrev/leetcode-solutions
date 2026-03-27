# Problem: Accounts Merge
# Language: python3
# Runtime: 220 ms
# Memory: 27.3 MB

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_name = {}
        graph = defaultdict(set)
        emails = set()
        names = [""] * len(accounts)
        for i,a in enumerate(accounts):
            name = a[0]
            if len(a) > 2:
                for u,v in zip(a[1:],a[2:]):
                    graph[u].add(v)
                    graph[v].add(u)
                    emails.add(u)
                    emails.add(v)
                    account_name[u] = i
                    account_name[v] = i
            else:
                account_name[a[1]] = i
                emails.add(a[1])
            names[i] = name
        
        
        seen = set()
        L = []
        def dfs(node):
            if node not in seen:
                seen.add(node)
                L.append(node)
                for n in graph[node]:
                    dfs(n)

        ans = []
        for n in emails:
            if n not in seen:
                L = []
                dfs(n)
                name = names[account_name[L[0]]]
                ans.append([name] + sorted(L))
        
        return ans
                