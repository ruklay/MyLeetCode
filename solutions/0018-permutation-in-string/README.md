# 18. Permutation in String

LeetCode Link: https://leetcode.com/problems/permutation-in-string/

## Description
The goal of the problem is to determine whether one string can be rearranged to form another string, essentially checking if the second string contains a permutation of the first string as a substring.

---

## Solution Approach
To solve the "Permutation in String" problem, we can use a sliding window approach along with character frequency counting. We maintain a frequency count of characters in the first string and compare it to the frequency count of characters in each substring of the second string that has the same length as the first string, updating the count as we slide the window across the second string.
