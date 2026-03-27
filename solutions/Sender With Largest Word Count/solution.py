# Problem: Sender With Largest Word Count
# Language: python3
# Runtime: 409 ms
# Memory: 21.9 MB

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        words = [len(m.split(" ")) for m in messages]
        c = Counter()
        for i,s in enumerate(senders):
            c[s] += words[i]
        
        A = [(v,k) for k,v in c.items()]
        A.sort(reverse=True)
        return A[0][1]