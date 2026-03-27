# Problem: Longest Absolute File Path
# Language: python3
# Runtime: 16 ms
# Memory: 14.2 MB

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        path = {0: 0}
        for line in input.splitlines():
            name = line.lstrip("\t")
            
            depth = len(line) - len(name)
            if "." in line:
                maxlen = max(maxlen, path[depth] + len(name))
            else:
                path[depth+1] = path[depth] + len(name) + 1
        
        return maxlen