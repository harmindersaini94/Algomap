def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target = "balloon"

        temp_dict = {}
        for i in text:
            if i in temp_dict:
                temp_dict[i] += 1
            else: temp_dict[i] = 1

        for c in target:
            if c not in temp_dict:
                return 0
        # this line makes sense because the min of these will be the max balloon we can male
        return min(temp_dict['b'], temp_dict['a'], temp_dict['l']//2, temp_dict['o']//2, temp_dict['n'])
        
            


                    


        