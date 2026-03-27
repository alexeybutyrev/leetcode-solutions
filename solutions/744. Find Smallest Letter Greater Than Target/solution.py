# Problem: Find Smallest Letter Greater Than Target
# Language: python3
# Runtime: 0 ms
# Memory: 20.8 MB

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ind = bisect_right(letters, target)
        return letters[ind if ind < len(letters) else 0]