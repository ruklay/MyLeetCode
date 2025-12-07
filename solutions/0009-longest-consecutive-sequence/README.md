# 9. Longest Consecutive Sequence

LeetCode Link: https://leetcode.com/problems/longest-consecutive-sequence/

## Description
The goal of the problem is to find the length of the longest sequence of consecutive integers within a given array, where the sequence can be formed by any combination of numbers present in the array.

---

## Solution Approach
To solve the "Longest Consecutive Sequence" problem, first convert the array into a set to allow for O(1) average time complexity lookups. Then, iterate through each number in the array, and for each number that is the start of a sequence (i.e., the number just before it is not in the set), count consecutive integers until the sequence ends, keeping track of the maximum length found.
