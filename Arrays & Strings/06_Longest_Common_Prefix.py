def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common = ""
        if len(strs) == 1:
            return strs[0]

        last = strs.pop()

        for s in strs:
            #here compare the last with all
            if common != "":
                minLen = min(len(common), len(s))
                i=0
                newcom = ""
                while(i<minLen):
                    if last[i] == s[i]:
                        newcom += last[i]
                    # Here if we want to check all common elements then remove this line
                    else : break
                    i += 1

                if newcom == "":
                    return ""
                elif newcom != common:
                    common = newcom
            else: 
                minLen = min(len(last), len(s))
                #print(minLen)
                i = 0
                while(i<minLen):
                    if last[i] == s[i]:
                        common += last[i]
                    # Here if we want to check all common elements then remove this line
                    else: break 
                    i += 1

                if common == "":
                    return ""

        return common


        