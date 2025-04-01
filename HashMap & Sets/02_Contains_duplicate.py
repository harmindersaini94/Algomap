def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        Since here we only need to know if there is any duplicate in the list
        so why not create a hashset here. set will have only unique values, and then
        we can compare the length of both the set and original list
        if same , means no duplicate return false, else return true
        '''

        # Method 1
        # unique = set(nums)
        # if len(unique) == len(nums):
        #     return False
        # else: return True

        # Method 2
        s = set()
        for i in nums:
            if i in s:
                return True
            else: s.add(i)
        return False


        