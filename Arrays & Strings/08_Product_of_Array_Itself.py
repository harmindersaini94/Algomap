def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        SO here scene ye hsi ki har number k left k sab aur right k sab ka product nikalo and multiply them
        '''
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n

        # ye kaise kaam kr rha hai ki agar aap ith position pr ho, toh i-1 hai jo left list la aur i-1 hai jo nums ka usse kro multiply and put it in ith of left
        # eg: agar index 2 pr hai hum, toh index 1 of left multiply it with index 1 of num
        for n in range(1, n):
            left[n] = left[n-1] * nums[n-1]
        print(left)

        # yha loop reverse chalao, again last position pr 1 hoga toh leave it, second last poisiton will have value of prod of last index of both array
        for n in range(len(nums), 1, -1):
            right[n-2] = right[n-1] * nums[n-1]
        print(right)

        
        for i in range(0, len(nums)):
            answer[i] = (left[i] * right[i])

        return answer





        
