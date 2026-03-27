# Problem: Baseball Game
# Language: python3
# Runtime: 44 ms
# Memory: 14.1 MB

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for a in ops:
            match a:
                case '+':
                    stack.append(str(int(stack[-1]) + int(stack[-2])))
                case 'D':
                    stack.append(str(int(stack[-1]) * 2))
                case 'C':
                    stack.pop()
                case _:
                    stack.append(a)
        
        return sum(map(int, stack))