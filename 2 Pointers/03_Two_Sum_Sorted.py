def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Since the Array is sorted, So we can use Two Pointer Directly
        left = 0
        right = len(numbers) - 1
        result = []

        while(left <= right):
            num_sum = numbers[left] + numbers[right]
            if num_sum == target:
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif num_sum < target:
                left += 1
            elif num_sum > target:
                right -= 1
        