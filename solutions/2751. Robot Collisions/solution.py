# Problem: Robot Collisions
# Language: python3
# Runtime: 1498 ms
# Memory: 47.1 MB

class Solution:
    def survivedRobotsHealths(self, P: List[int], H: List[int], D: str) -> List[int]:
        
        stack = []
        A = [(p,i,h,d) for i,(p,h,d) in enumerate(zip(P,H,D))]
        A.sort(key = lambda x: (x[0],x[1]))
        
        for p,i,h,d in A:
            if stack:

                if stack and stack[-1][-1] == 'R' and d == 'L' and stack[-1][-2] < h:
                    while stack and stack[-1][-1] == 'R' and d == 'L' and stack[-1][-2] < h:
                        p0,i0,h0,d0 = stack.pop()
                        h -= 1

                if stack and  stack[-1][-1] == 'R' and d == 'L' and stack[-1][-2] == h:
                    stack.pop()
                    continue
                
                if stack and  stack[-1][-1] == 'R' and d == 'L' and stack[-1][-2] > h:
                    p0,i0, h0,d0 = stack.pop()
                    stack.append((p0,i0,h0-1,d0))
                    continue
                
                stack.append((p,i,h,d))
            else:
                stack.append((p,i,h,d))
        
        stack.sort(key = lambda x: x[1])
        return [h for _,_,h,_ in stack]
    