def dailyTemperatures(temperatures):
        i = 0
        j = 1
        length = len(temperatures)
        answers = [0 for _ in range(length)]

        while i < length - 1:
            if temperatures[i] < temperatures[j]:
                answers[i] = j-i
                i += 1
                j = i + 1
            elif j <= length - 1:
                j += 1
            elif j == length:
                answers[i] = 0
                i += 1
                j = i + 1

        return answers

print(dailyTemperatures([73,74,75,71,69,72,76,73]))


        