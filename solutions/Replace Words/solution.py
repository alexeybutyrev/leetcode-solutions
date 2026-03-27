# Problem: Replace Words
# Language: python3
# Runtime: 103 ms
# Memory: 32.7 MB

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.is_word = False
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        if self.children:
            root = self.children[""]
        else:
            root = Trie()
        cur = root
        
        for l in word:
            if l not in cur.children:
                cur.children[l] = Trie()
            cur = cur.children[l]
        cur.is_word = True
        
        self.children[""] = root

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        if self.children:
            cur = self.children[""]
        else:
            return False
        
        for l in word:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        if self.children:
            cur = self.children[""]
        else:
            return False
        
        cur = self.children[""]
        
        for l in prefix:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return True
    
    def search_closest(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        if self.children:
            cur = self.children[""]
        else:
            return False
        
        word_return = ""
        for l in word:
            if l in cur.children:
                cur = cur.children[l]
                word_return += l
                if cur.is_word:
                    return word_return
            else:
                return word
        return word
    
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        t = Trie()
        for w in dict:
            t.insert(w)
        
        words = sentence.split(" ")
        for i in range(len(words)):
            #print("before - > ",words[i])
            words[i] = t.search_closest(words[i])
            #print("after - > ",words[i])
            
        return " ".join(words)