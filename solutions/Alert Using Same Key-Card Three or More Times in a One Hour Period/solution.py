# Problem: Alert Using Same Key-Card Three or More Times in a One Hour Period
# Language: python3
# Runtime: 800 ms
# Memory: 38.4 MB

from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def convert2sec(time):
            hours,minutes = time.split(":")
            if hours[0] == '0':
                hours = int(hours[1])
            else:
                hours = int(hours)
            
            if minutes[0] == '0':
                minutes = int(minutes[1])
            else:
                minutes = int(minutes)
            
            return hours * 3600 + minutes * 60
        
        n2t = defaultdict(list)
        n = len(keyName)
        
        for i in range(n):
            n2t[keyName[i]].append(convert2sec(keyTime[i]))
        
        #print(n2t)
        result = []
        for name in n2t:
            if len(n2t[name]) > 1:
                n2t[name].sort()
                #print(n2t[name])
                count = 1
                ind = 0
                for i in range(1,len(n2t[name])):
                    #print(n2t[name][ind],  n2t[name][i],  n2t[name][i] - n2t[name][ind], i, ind)
                    if n2t[name][i] - n2t[name][ind] <= 3600:
                        count += 1
                        if count ==3:
                            
                            result.append(name)
                            #print(result)
                            break
                    else:
                        while ind < i and n2t[name][i] - n2t[name][ind] > 3600:
                            #print("here")
                            ind += 1
                            count -= 1
                        count += 1
                        #print(ind, count) 
        
        result.sort()
        return result