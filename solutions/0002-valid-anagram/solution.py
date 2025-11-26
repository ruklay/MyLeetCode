from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    # Count the frequency of each character in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Compare the two frequency counts
    return count_s == count_t