# Approach 1
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        majority = {}
        for i in nums:
            if i in majority:
                majority[i] += 1
            else:
                majority[i] = 1

        maxim = float('-inf')
        actual_num = 0

        print(majority)

        for key,value in majority.items():
            maj = float(value) / 2
            print(maj)
            if maj > maxim:
                maxim = maj
                actual_num = key

        return actual_num
        