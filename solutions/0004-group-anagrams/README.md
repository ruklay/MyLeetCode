# 4. Group Anagrams

LeetCode Link: https://leetcode.com/problems/group-anagrams/

## Description
The goal of the "Group Anagrams" problem is to categorize a list of words into clusters where each cluster contains words that are anagrams of each other, meaning they can be rearranged to form one another. Essentially, you need to organize the words based on their letter compositions.

---

## Solution Approach
To solve the "Group Anagrams" problem, iterate through each word in the list, sort the characters of each word to create a unique key, and then use a dictionary to group words by their sorted key. Finally, return the values of the dictionary, which will contain lists of anagrams.
