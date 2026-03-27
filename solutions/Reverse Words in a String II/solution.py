# Problem: Reverse Words in a String II
# Language: python3
# Runtime: 216 ms
# Memory: 18.4 MB

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()
        N = len(s)
        i = j = 0
        while i < N and j < N:
            if s[j] == " ":
                s[i:j] = s[i:j][::-1] 
                i = j + 1
                j = j + 1
            j+=1
        s[i:j] = s[i:j][::-1] 
