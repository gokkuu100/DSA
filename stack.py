def is_balanced(expression):
    stack = []  

    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[': 
            stack.append(char)
        elif char in ')}]':  
            if not stack or stack[-1] != brackets_map[char]: 
                return False
            stack.pop()  

    return len(stack) == 0

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  
