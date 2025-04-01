def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else: s_dict[i] = 1

        for i in t:
            if i in s_dict:
                if s_dict[i] > 1:
                    s_dict[i] -= 1
                else: s_dict.pop(i)
            else: return False
        return True