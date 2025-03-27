def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romandict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        pairs = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
        }
        
        num = 0
        s_temp = s

        for pair in pairs:
            if pair in s_temp:
                s_temp = s_temp.replace(pair, "")
                num += pairs[pair]

        for c in s_temp:
            num += romandict[c]
        
        return num
        
