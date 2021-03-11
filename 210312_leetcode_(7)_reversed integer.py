class Solution:
    def reverse(self, x: int) -> int:
        
        minus = False
        
        if (x <= -(2^31)) or (x >= (2^31 - 1)):
            return 0
        
        if x < 0: 
            x *= (-1)
            minus = True
        
        y = list(str(x))
        y.reverse()
                  
        y = int(''.join(y))
        
        if minus == True:
            y *= (-1)

        return y