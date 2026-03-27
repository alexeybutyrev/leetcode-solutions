# Problem: First Letter to Appear Twice
# Language: python3
# Runtime: 66 ms
# Memory: 13.9 MB

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()
        for l in s:
            if l in st:
                return l
            st.add(l)
        