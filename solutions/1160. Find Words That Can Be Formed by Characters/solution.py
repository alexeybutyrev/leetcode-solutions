# Problem: Find Words That Can Be Formed by Characters
# Language: python
# Runtime: 428 ms
# Memory: 13.7 MB

from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c = Counter(chars)
        
        sm_ = 0
        for w in words:
            wc = Counter(w)
            if all(k in c and c[k] >= wc[k] for k,v in wc.items()):
                sm_ += len(w)
        return sm_
                