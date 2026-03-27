# Problem: Vowel Spellchecker
# Language: python3
# Runtime: 160 ms
# Memory: 17 MB

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        def encript(w):
            return "".join(["*" if l in 'aeiou' else l for l in w])
        
        
        perfect_words = set(wordlist)
        ans = []
        
        words_cap = {}
        words_vow = {}
        
        for w in wordlist:
            wlow = w.lower()
            if wlow not in words_cap:
                words_cap[wlow] = w
            
            wvow = encript(wlow)
            if wvow not in words_vow:
                words_vow[wvow] = w

        ans = []
        for q in queries:
            if q in perfect_words:
                ans.append(q)
                continue
            
            wlow = q.lower()
            if wlow in words_cap:
                ans.append(words_cap[wlow])
                continue
            
            wvow = encript(wlow)
            if wvow in words_vow:
                ans.append(words_vow[wvow])
                continue
            
            ans.append("")
        
        return ans