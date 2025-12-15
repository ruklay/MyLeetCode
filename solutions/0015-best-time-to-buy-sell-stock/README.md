# 15. Best Time to Buy & Sell Stock

LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Description
The problem involves determining the maximum profit that can be achieved by buying and selling a stock on different days, given a list of stock prices over time. The goal is to identify the optimal days to buy and sell to maximize the profit while ensuring that the selling day comes after the buying day.

---

## Solution Approach
To solve the "Best Time to Buy & Sell Stock" problem, iterate through the list of stock prices while maintaining the minimum price encountered so far. For each day's price, calculate the potential profit by subtracting the minimum price from the current price, and update the maximum profit if this potential profit exceeds the previously recorded maximum.
