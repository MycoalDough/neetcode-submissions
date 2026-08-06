class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ']' and len(stack) != 0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == '}' and len(stack) != 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif c == ')' and len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0