# 21. Valid Parentheses

LeetCode Link: https://leetcode.com/problems/valid-parentheses/

## Description
The goal of the "Valid Parentheses" problem is to determine whether a given string of parentheses is correctly balanced, meaning that every opening parenthesis has a corresponding closing parenthesis in the correct order.

---

## Solution Approach
To solve the "Valid Parentheses" problem, use a stack data structure to keep track of opening parentheses. Iterate through the string, pushing each opening parenthesis onto the stack and popping it when a corresponding closing parenthesis is encountered; at the end, the stack should be empty if the parentheses are balanced.
