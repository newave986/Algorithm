# leetcode 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        s = list(s)
        stack = []
        
        for x in s:
    
        
            if x == '(' or x == '[' or x == '{':
                stack.append(x)

            else:
                    
                if x == ')':
                    if stack[len(stack)-1] == '(':
                        del stack[len(stack)-1]
                    else:
                        return False

                elif x == ']':
                    if stack[len(stack)-1] == '[':
                        del stack[len(stack)-1]
                    else:
                        return False

                elif x == '}':
                    if stack[len(stack)-1] == '{':
                        del stack[len(stack)-1]
                    else:
                        return False
            
            
        if len(stack) != 0: return False
        else: return True