def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        left = 0
        right = len(height)-1

        while(left < right):
            min_ht = min(height[left], height[right])
            val = min_ht * (right - left)
            max_val = max(max_val, val)

            if height[left] < height[right]:
                left += 1
            else: right -= 1

        return max_val


            
        