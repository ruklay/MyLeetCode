from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        # Sort the word to create a key
        key = ''.join(sorted(word))
        # Append the original word to the list of its anagrams
        anagrams[key].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())