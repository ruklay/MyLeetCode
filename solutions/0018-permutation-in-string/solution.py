from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    len_s1, len_s2 = len(s1), len(s2)
    
    if len_s1 > len_s2:
        return False
    
    s1_count = Counter(s1)
    window_count = Counter(s2[:len_s1])
    
    if s1_count == window_count:
        return True
    
    for i in range(len_s1, len_s2):
        # Add the new character to the window
        window_count[s2[i]] += 1
        # Remove the character that is sliding out of the window
        window_count[s2[i - len_s1]] -= 1
        
        # If the count goes to zero, remove it from the counter
        if window_count[s2[i - len_s1]] == 0:
            del window_count[s2[i - len_s1]]
        
        # Compare the two counters
        if s1_count == window_count:
            return True
            
    return False