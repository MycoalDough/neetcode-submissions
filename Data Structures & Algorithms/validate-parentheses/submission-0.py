class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0