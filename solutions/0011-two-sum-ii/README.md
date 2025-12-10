# 11. Two Sum II

LeetCode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Description
The goal of the problem is to find two distinct numbers in a sorted array that add up to a specific target value, returning their indices. The solution should efficiently identify these indices while ensuring they are in ascending order.

---

## Solution Approach
To solve the "Two Sum II" problem, use a two-pointer technique: initialize one pointer at the beginning and the other at the end of the sorted array. Increment the left pointer or decrement the right pointer based on whether the sum of the values at these pointers is less than or greater than the target, until the correct pair is found.
