# 7. Valid Sudoku

LeetCode Link: https://leetcode.com/problems/valid-sudoku/

## Description
The goal of the "Valid Sudoku" problem is to determine whether a given 9x9 grid of numbers adheres to the rules of Sudoku, meaning that each row, column, and 3x3 subgrid contains the digits 1 through 9 without any repetitions.

---

## Solution Approach
To solve the "Valid Sudoku" problem, iterate through each cell in the 9x9 grid while maintaining three sets to track the numbers seen in each row, column, and 3x3 subgrid. If a number appears more than once in any of these sets, the Sudoku is invalid; otherwise, it is valid if all cells are checked without duplicates.
