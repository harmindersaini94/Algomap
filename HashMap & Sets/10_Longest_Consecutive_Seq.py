def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)
        length = 0

        '''
        So the idea here is that put the numbers in the set, then loop on the nums list
        for each num find num-1, if it is present, then it means the current number is not thr
        start of seq so we can continue
        but if num-1 is not present, then it means it is the start of seq
        so put length to 1, and find all the num+1 now that are in set
        once the while loop ends, update the length and continue
        '''

        for num in nums:
            if num-1 not in s:
                n_length = 1
                new_num = num + 1
                while(new_num in s):
                    n_length +=1
                    new_num += 1

                length = max(length, n_length)
        return length






        