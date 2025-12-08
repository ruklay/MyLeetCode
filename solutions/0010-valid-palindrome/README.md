# 10. Valid Palindrome

LeetCode Link: https://leetcode.com/problems/valid-palindrome/

## Description
The goal of the "Valid Palindrome" problem is to determine whether a given string reads the same forwards and backwards when ignoring non-alphanumeric characters and case differences.

---

## Solution Approach
To solve the "Valid Palindrome" problem, iterate through the string while using two pointers: one starting from the beginning and the other from the end. Compare the characters at these pointers, skipping non-alphanumeric characters and ignoring case differences, until the pointers meet; if all corresponding characters match, the string is a valid palindrome.
