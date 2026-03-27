# Problem: Open the Lock
# Language: python3
# Runtime: 595 ms
# Memory: 15.9 MB

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        hm = {'0':'19', '1':'02', '2':'13', '3':'42', '4':'53', '5':'64', '6':'75', '7':'86', '8':'97', '9':'08'}
        
        if target == '0000':
            return 0
        q = [('0000',0)]
        seen = set(deadends) 
        if '0000' in seen:
            return -1
        
        seen |= {'0000'}
        
         
        def generate(c,i):
            ans =set()
            for i in range(4):
                for l in hm[c[i]]:
                    ans.add(c[:i] + l + c[i+1:])
            return ans
        
        #print(generate('0000',0))
        #return 1
        for c,count in q:
            #print(q)
            if c == target:
                return count
            
            for x in generate(c,0):
                if x not in seen:
                    seen.add(x)
                    q.append((x,count + 1))
        
        return -1
                