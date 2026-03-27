# Problem: Last Visited Integers
# Language: python3
# Runtime: 66 ms
# Memory: 16.3 MB

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = []
        stack = []
        c = 0
        for i,w in enumerate(words):
            if w == "prev":
                c += 1
                if len(stack) >= c:
                    ans.append(stack[-c])
                else:
                    ans.append(-1)
            else:
                c = 0
                stack.append(int(w))
        return ans