# Problem: Letter Case Permutation
# Language: python3
# Runtime: 52 ms
# Memory: 14.6 MB

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        N = len(S)
        ans = [""]
        
        for l in S:
            A = []
            for a in ans:
                if l.isalpha():
                    A.append(a + l.lower())
                    A.append(a + l.upper())
                else:
                    A.append(a + l)
                ans = A
        return ans