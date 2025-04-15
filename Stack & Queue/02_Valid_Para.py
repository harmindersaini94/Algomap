def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        So logic ye hai ki opening para ko stack me push krdo, jab bhi closing para detect hogs
        to stack se pop kro, pop krne se pehle check stack size, and if popped element is the matching continue,    
        else return false
        '''
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            if i == ')':
                if len(stack) > 0:  
                    a = stack.pop()
                    if a != '(':
                        return False
                else: return False
            if i == '}':
                if len(stack) > 0: 
                    a = stack.pop()
                    if a != '{':
                        return False
                else: return False
            if i == ']':
                if len(stack) > 0: 
                    a = stack.pop()
                    if a != '[':
                        return False
                else: return False
        if len(stack) > 0:
            return False
        return True