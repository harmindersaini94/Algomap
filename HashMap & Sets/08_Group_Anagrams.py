def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def sortStrChar(word):
            '''
            1. convert str into char list
            2. sort the list
            3. convert list to str
            4. return
            '''
            char_list = list(word)
            char_list.sort()
            return "".join(char_list)

        
        word_dict = {}
        for word in strs:
            sorted_word = sortStrChar(word)

            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else: word_dict[sorted_word] = [word]
        
        list_final = []
        for key,value in word_dict.items():
            list_final.append(value)

        return list_final
        