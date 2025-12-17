# 16. Longest Substring Without Repeating Characters

LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Description
The goal of the problem is to find the length of the longest contiguous segment of characters in a given string where no character appears more than once. This involves efficiently tracking characters and their positions to ensure uniqueness within the substring.

---

## Solution Approach
To solve the "Longest Substring Without Repeating Characters" problem, use a sliding window approach with two pointers to maintain the current substring, while utilizing a hash set to track characters and their positions. As you iterate through the string, expand the window by moving the right pointer and contract it by moving the left pointer whenever a duplicate character is encountered, updating the maximum length of the substring as needed.
