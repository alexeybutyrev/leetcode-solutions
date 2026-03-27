# Problem: Destination City
# Language: python3
# Runtime: 55 ms
# Memory: 16.4 MB

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = {x for x,y in paths}
        for x,y in paths:
            if y not in s:
                return y