# 2. Valid Anagram

LeetCode Link: https://leetcode.com/problems/valid-anagram/

## Description
The task is to determine whether two given strings are anagrams of each other, meaning they contain the same characters in the same frequency but may be arranged in a different order.

---

## Solution Approach
To determine if two strings are anagrams, we can count the frequency of each character in both strings using a hash map or an array, then compare the two frequency counts. If the counts match for all characters, the strings are anagrams; otherwise, they are not.
