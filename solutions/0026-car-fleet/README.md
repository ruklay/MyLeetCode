# 26. Car Fleet

LeetCode Link: https://leetcode.com/problems/car-fleet/

## Description
The "Car Fleet" problem involves determining how many groups of cars, traveling towards a destination at varying speeds, will arrive together at that destination, considering that faster cars can catch up to slower ones. The goal is to calculate the number of distinct fleets formed based on their starting positions and speeds.

---

## Solution Approach
To solve the "Car Fleet" problem, first, sort the cars by their starting positions in descending order. Then, calculate the time it takes for each car to reach the destination, and group cars into fleets based on whether a faster car can catch up to a slower one, counting distinct fleets as you iterate through the sorted list.
