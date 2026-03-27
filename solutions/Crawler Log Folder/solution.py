# Problem: Crawler Log Folder
# Language: python3
# Runtime: 44 ms
# Memory: 14.2 MB

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ind = 0
        for l in logs:
            if l == "./":
                continue
            elif l == "../":
                ind = max(0,ind -1)
            else:
                ind += 1
        
        return max(0,ind)