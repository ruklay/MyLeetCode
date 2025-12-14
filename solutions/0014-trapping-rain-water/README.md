# 14. Trapping Rain Water

LeetCode Link: https://leetcode.com/problems/trapping-rain-water/

## Description
The "Trapping Rain Water" problem involves calculating the total amount of water that can be trapped between various heights of terrain after it rains, based on the elevation map represented by an array of integers. The goal is to determine how much water would accumulate in the dips and valleys formed by the heights.

---

## Solution Approach
To solve the "Trapping Rain Water" problem, we can use a two-pointer approach where we maintain two pointers at the beginning and end of the elevation array, along with two variables to track the maximum heights encountered from both sides. By iterating towards the center, we can calculate the trapped water at each position based on the minimum of the maximum heights, updating the pointers and maximums accordingly.
