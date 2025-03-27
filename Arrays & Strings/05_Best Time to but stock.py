def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0

        # non-optimized
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > max:
        #             max = profit
        # return max

        max_profit = 0
        min_price = float('inf')
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit

        
        return max_profit