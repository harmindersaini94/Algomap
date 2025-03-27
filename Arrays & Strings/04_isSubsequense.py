def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0

        lens = len(s)
        lent = len(t)
        found = 0

        while (i < lens and j < lent):
            if s[i] == t[j]:
                found += 1
                i += 1
                j += 1
            else:
                j += 1

        
        if found == lens:
            return True
        else: return False