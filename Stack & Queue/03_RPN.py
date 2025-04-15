def evalRPN(tokens):
        import math
        """
        :type tokens: List[str]
        :rtype: int
        """
        arr = []
        for i in tokens:
            if i == '+' or i == '-' or i == '/' or i == '*':
                b = arr.pop()
                a = arr.pop()
                if i == '+':
                    arr.append(a+b)
                elif i == '-':
                    arr.append(a-b)
                elif i == '/':
                    arr.append(math.trunc(a/b))
                elif i == '*':
                    arr.append(a*b)
            else: arr.append(int(i))
        
        return arr[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

        