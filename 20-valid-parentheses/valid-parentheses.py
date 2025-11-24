class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False

        for char in s:
            if char == '(':
                stack.append(char)
            if char == '{':
                stack.append(char)
            if char == '[':
                stack.append(char)    

            if char == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if char == '}':
                if stack:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if char == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return not bool(stack)           