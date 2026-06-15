class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        #while '()' in s or '[]' in s or '{}' in s:
        #    s = s.replace('()', '')
        #    s = s.replace('[]', '')
        #    s = s.replace('{}', '')
        #return s == ''
        
        stack = []
        d = {')' : '(', ']' : '[', '}' : '{'}
        
        for l in s:
            if l in d:
                if stack and stack[-1] == d[l]:
                    stack = stack[:-1]
                else:
                    return False            
            else:
                stack.append(l)
        return stack == []
                
                    
