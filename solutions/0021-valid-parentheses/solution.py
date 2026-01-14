def is_valid_parentheses(s: str) -> bool:
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in parentheses_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in parentheses_map.keys():  # If it's a closing bracket
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()
    
    return not stack  # If stack is empty, parentheses are balanced

# Example usage:
# result = is_valid_parentheses("()[]{}")
# print(result)  # Output: True