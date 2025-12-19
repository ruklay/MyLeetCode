def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_count = 0
    count = [0] * 26  # To count the frequency of each character (assuming only uppercase letters)

    for right in range(len(s)):
        # Increment the count of the current character
        count[ord(s[right]) - ord('A')] += 1
        # Update the max_count of the most frequent character in the current window
        max_count = max(max_count, count[ord(s[right]) - ord('A')])

        # If the number of characters to replace exceeds k, shrink the window
        if (right - left + 1) - max_count > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1

    return len(s) - left + max_count - 1  # Return the length of the longest valid substring