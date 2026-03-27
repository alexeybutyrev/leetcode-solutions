# Problem: Remove All Adjacent Duplicates in String II
# Language: python3
# Runtime: 64 ms
# Memory: 15.7 MB

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        ans = ""
        for l in s:
            if stack and stack[-1][0] == l:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([l,1])
        
        for l,c in stack:
            ans += l * c
        
        return ans