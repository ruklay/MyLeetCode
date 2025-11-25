# 1. Contains Duplicate

LeetCode Link: https://leetcode.com/problems/contains-duplicate/

## Description
The goal of the "Contains Duplicate" problem is to determine whether a given collection of numbers includes any value that appears more than once. You need to identify if there are duplicates within the dataset.

---

## Solution Approach
To solve the "Contains Duplicate" problem, you can utilize a hash set to track the numbers as you iterate through the collection. For each number, check if it already exists in the set; if it does, a duplicate is found, otherwise, add the number to the set and continue.
