# 12. 3Sum

LeetCode Link: https://leetcode.com/problems/3sum/

## Description
The "3Sum" problem involves finding all unique sets of three numbers from a given list that add up to zero. The challenge lies in efficiently identifying these combinations while avoiding duplicates.

---

## Solution Approach
To solve the "3Sum" problem, first, sort the input list, then use a two-pointer technique to iterate through the list while fixing one number and searching for pairs that sum to the negative of the fixed number. This approach helps efficiently find unique triplets while avoiding duplicates by skipping over repeated elements.
