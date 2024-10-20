def removeOuterParentheses(s: str) -> str:
        
    count = 0
    result = []
    for char in s:
        if char == "(":
            count += 1
            if count > 1:
                result.append(char)
        else:
            count -= 1
            if count > 0:
                result.append(char)
    return ''.join(result)
s = "(()())(())"
print(removeOuterParentheses(s))