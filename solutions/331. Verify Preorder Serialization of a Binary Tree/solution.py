# Problem: Verify Preorder Serialization of a Binary Tree
# Language: python3
# Runtime: 38 ms
# Memory: 14.2 MB

import re
class Solution:
    def isValidSerialization(self, S: str) -> bool:
        
        while S:
            s2 = re.sub("([0-9]+),#,#","#", S) # replace node.val,#,# -> #
            
            # if it's # means we reached the final node and it's good
            if s2 == "#": return True         
            
            # if the lenght didn't change means the format is messed up
            if len(s2) == len(S): return False
            S = s2
        