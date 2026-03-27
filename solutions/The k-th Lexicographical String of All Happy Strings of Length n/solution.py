# Problem: The k-th Lexicographical String of All Happy Strings of Length n
# Language: python3
# Runtime: 35 ms
# Memory: 19.4 MB

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        q = deque(["a","b","c"])
        for _ in range(n-1):
            L = len(q)
            for __ in range(L):
                s = q.popleft()
                for x in 'abc':
                    if s[-1] !=x:
                        q.append(s + x)
        
        return "" if len(q) < k else q[k-1]