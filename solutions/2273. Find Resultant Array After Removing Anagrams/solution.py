# Problem: Find Resultant Array After Removing Anagrams
# Language: python3
# Runtime: 23 ms
# Memory: 18 MB

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        ans = [words[0]]
        j = 1
        while j < len(words):
            C = Counter(ans[-1])
            while j < len(words) and Counter(words[j]) == C:
                j+=1
            if j < len(words):
                ans.append(words[j])
                j+=1
        return ans

        