class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #loop through the array and have a buy min,left ptr
        #loop thorugh array and if you see a number less than the left
        #move that to the number u saw that at
        #the right pointer will keep moving at same time time cal profit
        #so we have to do sell - buy and get maxo if

        buy = prices[0] 
        profit = 0
        maxP = 0
        for i in range(len(prices)):

            if prices[i] < buy:
                buy = prices[i]

            profit = prices[i] - buy
            maxP = max(profit,maxP)

        return maxP
