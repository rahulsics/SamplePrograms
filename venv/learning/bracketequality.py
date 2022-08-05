from datetime import time
s = "][{{21}(3{()}3)}11{}]"


def check(s):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    stack = []
    for i in s:
        if i in opening:
            stack.append(i)
        elif i in closing:
            popped = stack.pop()
            if i == ')':
                if popped != '(':
                    return False
            if i == ']':
                if popped != '[':
                    return False
            if i == '}':
                if popped != '{':
                    return False


status = check(s)
if not status:
    print("Mismatch Parenthesis")

else:
    print("Matching Parenthesis")
