def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)
        stack = []
        answers = [0] * len(temperatures)

        for i in range(length):
            curr_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < curr_temp:
                prev = stack.pop()
                answers[prev] = i - prev
            stack.append(i)
        return answers