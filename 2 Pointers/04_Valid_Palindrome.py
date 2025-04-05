def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_list = []

        for i in s:
            if i.isalnum():
                str_list.append(i.lower())

        newstr = "".join(str_list)
        left = 0
        right = len(newstr) - 1

        while(left <= right):
            if (newstr[left] == newstr[right]):
                left += 1
                right -= 1
            else: return False
        return True
        