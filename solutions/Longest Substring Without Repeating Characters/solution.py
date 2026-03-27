# Problem: Longest Substring Without Repeating Characters
# Language: python
# Runtime: 56 ms
# Memory: 13.7 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        i = 0
        j = 0
        ans = 0
        st = set()
        while i < N and j < N:
            while s[j] in st:
                st.remove(s[i])
                i+=1
            st.add(s[j])
            ans = max(ans, 1 + j - i)
            j += 1
        return ans