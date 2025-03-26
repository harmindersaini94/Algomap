def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest_dist = float('inf')
        close_to_zero = float('-inf')

        for n in nums:
            dist = abs(n) 
            if dist < smallest_dist:
                smallest_dist = dist
                close_to_zero = n
            elif dist == smallest_dist:
                if n > close_to_zero:
                    close_to_zero = n

        return close_to_zero