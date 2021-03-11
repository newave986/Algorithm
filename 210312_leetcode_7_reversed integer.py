# leetcode #7 reversed integer 

class Solution:
    def reverse(self, x: int) -> int:
        
        minus = False
        
        if x < 0: 
            x *= (-1)
            minus = True
        
        y = list(str(x))
        y.reverse()
                  
        y = int(''.join(y))
        
        if minus == True:
            y *= (-1)
            
        if (y <= -(2**31)) or (y >= (2**31 - 1)): return 0
        else: return y
