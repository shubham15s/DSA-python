def is_balanced(parens):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in parens:
        if char in pairs.values():  
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or stack.pop() != pairs[char]: 
                return False
    return stack == []

test_strings = [
    "()",        # Balanced
    "(())",      # Balanced
    "({[]})",    # Balanced
    "((",        # Not Balanced
    ")",         # Not Balanced
    "({[)]}",    # Not Balanced
    "((()))",    # Balanced
    "([{}])",    # Balanced
    "((())",     # Not Balanced
]

for s in test_strings:
    print(f"{s}: {'Balanced' if is_balanced(s) else 'Not Balanced'}")
