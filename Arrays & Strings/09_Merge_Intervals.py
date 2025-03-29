def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        merged_list = []

        #sort intervals first based on the starting point
        intervals.sort(key=lambda x:x[0])

        for x in intervals:
            if len(merged_list) > 0:
                y = merged_list[-1]

                if y[1] >= x[0]:
                    merged_list[-1] = [y[0], max(y[1], x[1])]
                else: merged_list.append(x)
            else:
                # means merged list is empty, it will be during the start
                merged_list.append(x)

        return merged_list
        