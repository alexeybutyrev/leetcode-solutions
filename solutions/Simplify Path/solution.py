# Problem: Simplify Path
# Language: python3
# Runtime: 16 ms
# Memory: 14.4 MB

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.rstrip("/")
        i = 0
        N = len(path)
        stack = []
        
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif not p or p == ".":
                continue
            else:
                stack.append(p)
        return "/" + "/".join(stack)