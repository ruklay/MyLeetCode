# 13. Container with Most Water

LeetCode Link: https://leetcode.com/problems/container-with-most-water/

## Description
The problem involves finding two vertical lines on a coordinate plane that, together with the x-axis, form a container capable of holding the maximum amount of water. The goal is to determine the maximum area that can be enclosed by these lines.

---

## Solution Approach
To solve the "Container with Most Water" problem, use a two-pointer approach by initializing one pointer at each end of the array and iteratively calculating the area formed by the lines at these pointers. Move the pointer pointing to the shorter line inward to potentially find a taller line that could increase the area, repeating this process until the pointers meet, while keeping track of the maximum area encountered.
