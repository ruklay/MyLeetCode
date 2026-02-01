# 25. Daily Temperatures

LeetCode Link: https://leetcode.com/problems/daily-temperatures/

## Description
The goal of the problem is to determine how many days one must wait until a warmer temperature occurs for each day in a given list of daily temperatures. This involves analyzing the list to find the next higher temperature for each day and counting the intervening days.

---

## Solution Approach
To solve the "Daily Temperatures" problem, we can use a stack to keep track of the indices of the temperatures as we iterate through the list. For each temperature, we pop from the stack until we find a warmer temperature, allowing us to calculate the number of days until that warmer temperature occurs for each day.
