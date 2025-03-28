class Solution(object):
    def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        range_list = []
        range_str = ""
        prev = ""

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            range_list.append(str(nums[0]))
            return range_list
        else:
            for n in range(0,len(nums)):
                if n == 0:
                    range_str = str(nums[n]) + "->"
                    prev = str(nums[n])

                    print("n = 0 ", range_str, prev)
                    continue

                if nums[n] - int(prev) == 1:
                    prev = str(nums[n])
                    print(prev)
                else:
                    #close prev range and start a new range
                    if prev in range_str:
                        range_str = prev
                    else: 
                        range_str += prev

                    range_list.append(range_str)
                    range_str = str(nums[n]) + "->"
                    prev = str(nums[n])

            if prev in range_str:
                range_str = prev
            else: 
                range_str += prev

            range_list.append(range_str)

            return range_list

                

    print(summaryRanges([0,1,2,4,5,7]))