def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        final_list = []
        n = len(intervals)
        merged = []

        if n == 1:
            return intervals

        for item in range(1, n):
            list_i_1 = intervals[item-1] #[8,10]
            list_i = intervals[item] #[15,18]

            if list_i_1[1] >= list_i[0]:
                final_list.append([list_i_1[0], list_i[1]]) #[1,6] [8,10]
                merged = list_i #[]
            else:
                if list_i_1 == merged:
                    #final_list.append(list_i) #[1,6] [8,10]
                    merged = []
                else: final_list.append(list_i_1)

                if list_i == merged:
                    #final_list.append(list_i) #[1,6] [8,10]
                    merged = []
                else: final_list.append(list_i)

        return final_list

