# Problem: Unique Email Addresses
# Language: python3
# Runtime: 60 ms
# Memory: 14.4 MB

from re import sub
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            e = sub('\+.+@','@',e)
            name,domain = e.split('@') 
            name = sub('\.','', name)
            s.add(name + '@' + domain)
            
        return len(s)