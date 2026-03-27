# Problem: Goat Latin
# Language: python3
# Runtime: 24 ms
# Memory: 12.7 MB

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        l = S.split(" ")
        a_ind = 0
        return_str = ""
        for w in l:
            a_ind+=1
            if w[0].lower() in vowel:
                return_str+= w + 'ma' + 'a' * a_ind + " "
            else:
                return_str += w[1:] + w[0] + 'ma' + 'a' * a_ind + " "
        
        return return_str[:-1]