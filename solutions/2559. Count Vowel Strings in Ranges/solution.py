# Problem: Count Vowel Strings in Ranges
# Language: python3
# Runtime: 663 ms
# Memory: 54.8 MB

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        A = [0]
        for w in words:
            s = 0
            if w[0] in {'a', 'e', 'i', 'o', 'u'} and w[-1] in {'a', 'e', 'i', 'o', 'u'}:
                s+=1
            A.append(A[-1] + s)
        print(A)
        ans = []
        for l,r in queries:
            ans.append(A[r+1] - A[l])
        return ans