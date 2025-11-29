# 3. Two Sum

LeetCode Link: https://leetcode.com/problems/two-sum/

## Description
The "Two Sum" problem involves finding two distinct numbers in a list that add up to a specified target value. The goal is to identify the indices of these two numbers efficiently.

---

## Solution Approach
To solve the "Two Sum" problem efficiently, use a hash map to store each number's index as you iterate through the list. For each number, check if the complement (target minus the current number) exists in the hash map; if it does, return the indices of the current number and its complement.
