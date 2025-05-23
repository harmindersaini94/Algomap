def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        result = []

        # our objective here is to create a array in descening order and then reverse it
        # creating a descending order array
        while left <= right:
            if abs(nums[left]) < abs(nums[right]): 
                #move right 
                result.append(nums[right] * nums[right])
                right -= 1
            else:
                result.append(nums[left] * nums[left])
                left += 1
        result.reverse()
        return result

        