# Problem: Maximum Repeating Substring
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ind = sequence.find(word, 0)
        if ind < 0:
            return 0
        count = 1
        nw = len(word)
        max_count = 1
        
        while ind >= 0:
            old_ind = ind
            ind = sequence.find(word, old_ind+nw)
            #print(old_ind, ind)
            if ind - old_ind == nw:
                count +=1 
                max_count = max(count, max_count)
            else:
                count = 1
                
        return max_count
            