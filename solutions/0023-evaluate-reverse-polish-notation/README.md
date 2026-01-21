# 23. Evaluate Reverse Polish Notation

LeetCode Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Description
The task is to compute the result of a mathematical expression given in Reverse Polish Notation (RPN), where operators follow their operands, allowing for the evaluation of expressions without the need for parentheses. The goal is to process a list of tokens representing numbers and operators, and return the final calculated value.

---

## Solution Approach
To evaluate an expression in Reverse Polish Notation, use a stack to store operands. Iterate through the list of tokens; for each number, push it onto the stack, and for each operator, pop the required number of operands from the stack, perform the operation, and push the result back onto the stack, ultimately returning the final value at the top of the stack.
