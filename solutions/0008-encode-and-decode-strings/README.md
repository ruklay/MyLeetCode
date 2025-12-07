# 8. Encode and Decode Strings

LeetCode Link: https://leetcode.com/problems/encode-and-decode-strings/

## Description
The task involves creating a method to convert a list of strings into a single encoded string and then decoding that string back into the original list, ensuring that the process accurately preserves the content and order of the strings.

---

## Solution Approach
To solve the "Encode and Decode Strings" problem, we can concatenate the strings in the list using a unique delimiter that does not appear in any of the strings, followed by encoding the length of each string. For decoding, we can split the encoded string by the delimiter and reconstruct the original list by reading the lengths of the individual strings.
