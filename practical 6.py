def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expr):
    stack, postfix = [], ""
    for ch in expr:
        if ch == ' ':
            continue
        if ch.isalnum():                      # operand
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()                       # remove '('
        else:                                 # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()
            stack.append(ch)
    while stack:
        postfix += stack.pop()
    return postfix

def evaluate_postfix(postfix):
    stack = []
    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+': stack.append(a + b)
            elif ch == '-': stack.append(a - b)
            elif ch == '*': stack.append(a * b)
            elif ch == '/': stack.append(a / b)
    return stack.pop()

# Main
infix = input("Enter infix expression: ")
postfix = infix_to_postfix(infix)
print("Postfix Expression:", postfix)

if all(c.isdigit() or c in "+-*/" for c in postfix):
    print("Evaluation Result:", evaluate_postfix(postfix))
else:
    print("Evaluation skipped (expression contains variables, not digits).")
