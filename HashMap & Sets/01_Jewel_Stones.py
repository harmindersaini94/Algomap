def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int

        Logic, Two things we need to do here
        1. Find if jewel char is in stones
        2. if yes count how many, coz each will be a jewel
        """

        stones_set = set(stones)
        total_stones = 0

        # one important thing that we did in this is to convert the stones string to set
        # why coz, I know that to know if a jewel is a stone, I need to look up in string
        # since loopuo is contant for set, so convert it into set and then count
        for jewel in jewels:
            if jewel in stones_set:
               total_stones += stones.count(jewel)
        return total_stones

        