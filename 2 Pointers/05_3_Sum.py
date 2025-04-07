def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visited = []

        len_num = len(nums)-1

        result = []
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            
            left = i+1
            right = len_num

            absVal = 0
            if nums[i] == 0:
                absVal = 0
            elif nums[i] > 0:
                absVal = 0 - nums[i]
            elif nums[i] < 0:
                absVal = abs(nums[i])

            while(left < right):
                summ = nums[left] + nums[right]
                if summ == absVal:
                    visited.append(nums[i])
                    list_temp = [nums[i], nums[left], nums[right]]
                    list_temp.sort()
                    if list_temp not in result:
                        result.append(list_temp)

                    left += 1
                    right -= 1
                elif summ > absVal:
                    right -= 1
                elif summ < absVal:
                    left += 1
                    
        return result