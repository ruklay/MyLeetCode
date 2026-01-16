# 22. Min Stack

LeetCode Link: https://leetcode.com/problems/min-stack/

## Description
The "Min Stack" problem involves designing a stack data structure that not only supports standard stack operations like push and pop but also allows for retrieving the minimum element in constant time. The challenge is to efficiently manage the storage of elements and track the minimum value as items are added or removed.

---

## Solution Approach
To solve the "Min Stack" problem, maintain two stacks: one for the regular stack operations and another for tracking the minimum values. When pushing an element, compare it with the current minimum and push it onto the min stack only if it is smaller or equal, ensuring that the top of the min stack always reflects the current minimum value.
