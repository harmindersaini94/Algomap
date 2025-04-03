def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in num_dict:
                return [i, num_dict[diff]]
            else: num_dict[nums[i]] = i
        