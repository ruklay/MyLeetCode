# 20. Sliding Window Maximum

LeetCode Link: https://leetcode.com/problems/sliding-window-maximum/

## Description
The goal of the "Sliding Window Maximum" problem is to efficiently find the largest value in a subarray of a specified size as it moves across a larger array, updating the maximum value each time the window shifts. This requires optimizing the process to avoid recalculating the maximum from scratch for each new position of the window.

---

## Solution Approach
To solve the "Sliding Window Maximum" problem efficiently, we can use a deque (double-ended queue) to maintain the indices of the elements in the current window, ensuring that the largest element's index is always at the front. As we slide the window across the array, we remove indices that are out of the window's range and discard smaller elements from the back of the deque, allowing us to retrieve the maximum in constant time.
