# Problem: Palindrome Partitioning
# Language: python3
# Runtime: 450 ms
# Memory: 35.3 MB

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        N = len(s)
        def walk(i,A):
            if i == N:
                if A and A[-1] and A[-1] == A[-1][::-1]:
                    ans.append(A)
            else:
                if A and A[-1] and A[-1] == A[-1][::-1]:
                    walk(i+1,A[:] + [s[i]])
                A[-1] += s[i]
                walk(i+1,A)
        walk(0,[""])
        return ans
            