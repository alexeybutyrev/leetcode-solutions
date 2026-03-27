# Problem: Reformat Date
# Language: python3
# Runtime: 44 ms
# Memory: 13.8 MB

class Solution:
    def reformatDate(self, date: str) -> str:
        ms = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        hm = {ms[i]: "0" + str(i +1) if i not in[9,10,11] else str(i+1) for i in range(len(ms))}
        d = date.split(" ")
        #print(hm)
        
        dd = ""
        for i in range(len(d[0])):
            if d[0][i].isdigit():
                dd = dd + d[0][i]
            else:
                break
        dd = dd if len(dd) > 1 else "0" + dd
        mm = hm[d[1]]
        
        return d[2] + '-' + mm + '-' + dd
        