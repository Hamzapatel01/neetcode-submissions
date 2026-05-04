class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #make a pointer left that will be on day 0
        #make a right pointer to keep track of the sell
        #track the max of sell-buy and update it accordingly
        #if at any point of right you see a price less than prices[left]
        #keep the left pointer at that point and move the right pointer and recal profit

        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            maxProfit = max(profit, maxProfit)
            if prices[sell] < prices[buy]:
                buy = sell           
            sell+=1
        return maxProfit