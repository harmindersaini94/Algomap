def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in operations:
            if i == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif i == 'D':
                a = stack[-1]
                stack.append(a*2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)

        