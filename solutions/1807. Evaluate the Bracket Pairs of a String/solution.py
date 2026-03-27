# Problem: Evaluate the Bracket Pairs of a String
# Language: python3
# Runtime: 1292 ms
# Memory: 54.7 MB

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        hm = defaultdict(lambda : "?")
        for u,v in knowledge:
            hm[u] = list(v)
        stack = []
        
        for l in s:
            if l == ")":
                w = ""
                while stack and stack[-1] != "(":
                    w = stack.pop() + w
                
                stack.pop()
                stack += hm[w]
            else:
                stack.append(l)
        
        return "".join(stack)