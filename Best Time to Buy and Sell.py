#https://www.designgurus.io/viewer/document/grokking-the-coding-interview/6516a68866622b0a42a0a781
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
