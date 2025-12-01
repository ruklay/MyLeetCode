# 5. Top K Frequent Elements

LeetCode Link: https://leetcode.com/problems/top-k-frequent-elements/

## Description
The task is to identify the most frequently occurring elements in a given collection and return a specified number of these top elements. The challenge lies in efficiently determining which elements appear the most often within the dataset.

---

## Solution Approach
To solve the "Top K Frequent Elements" problem, first, use a hash map to count the frequency of each element in the collection. Then, utilize a min-heap to efficiently extract the top K elements with the highest frequencies.
