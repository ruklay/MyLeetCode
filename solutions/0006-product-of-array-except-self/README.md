# 6. Product of Array Except Self

LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/

## Description
The task is to create an array where each element is the product of all the numbers in the original array except for the number at that specific index, without using division and while maintaining an efficient time complexity.

---

## Solution Approach
To solve the "Product of Array Except Self" problem, we can use two auxiliary arrays: one to store the cumulative product of elements to the left of each index and another for the cumulative product of elements to the right. By multiplying the corresponding values from these two arrays, we can construct the result array without using division and in linear time complexity.
