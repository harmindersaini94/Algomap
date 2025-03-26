def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        #Find the length of both the words, loop on the smallest
        #Take the substring of the biggest and merge the rest of it with result

        len1 = len(word1)
        len2 = len(word2)
        finalStr = ""

        if len1 > len2:
            for eachChar in range(0,len2):
                finalStr = finalStr + word1[eachChar] + word2[eachChar]
            
            finalStr = finalStr + word1[len2:]
        elif len2 > len1:
            for eachChar in range(0,len1):
                finalStr = finalStr + word1[eachChar] + word2[eachChar]

            finalStr = finalStr + word2[len1:]
        else:
            for eachChar in range(0,len1):
                finalStr = finalStr + word1[eachChar] + word2[eachChar] 
        
        return finalStr