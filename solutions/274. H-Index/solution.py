# Problem: H-Index
# Language: python3
# Runtime: 36 ms
# Memory: 14 MB


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        N = len(citations)

        citations.sort()
        count = 0
        #citations[citations.length - 1 - i] > i
        
        while count < N and citations[N -count-1] > count:
            count +=1
        return count