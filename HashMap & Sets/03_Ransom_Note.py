def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        '''
        One approach that come to my mind here is that 
        create dictionary in both and then compare
        '''
        # Method 1
        # ransom_dict = {}
        # for a in ransomNote:
        #     if a in ransom_dict:
        #         ransom_dict[a] += 1
        #     else: ransom_dict[a] = 1

        # magazine_dict = {}
        # for a in magazine:
        #     if a in magazine_dict:
        #         magazine_dict[a] += 1
        #     else: magazine_dict[a] = 1

        # for key,value in ransom_dict.items():
        #     if key in magazine_dict:
        #         if value > magazine_dict[key]:
        #             return False
        #     else: return False
        # return True

        # Method 2
        magazine_dict = {}
        for a in magazine:
            if a in magazine_dict:
                magazine_dict[a] += 1
            else: magazine_dict[a] = 1

        # Now we will loop thru the notes, and for each key, we decrement the counter
        # if we have a key with count 1, then we remove it, coz if we put zero then we still
        # have the key

        for a in ransomNote:
            if a in magazine_dict:
                if magazine_dict[a] > 1:
                    magazine_dict[a] -= 1
                else: magazine_dict.pop(a)
            else: return False
        return True
