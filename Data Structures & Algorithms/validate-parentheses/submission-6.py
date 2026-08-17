class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        start = ['(', '[', '{']
        stop = [')', ']', '}']
        for char in s:
            if char in start:
                stack.append(char)
            elif char in stop:
                if not stack:
                    return False
                last = stack.pop()
                if char == ')' and last == '(':
                    continue
                if char == ']' and last == '[':
                    continue
                if char == '}' and last == '{':
                    continue
                else:
                    return False
        
        return not stack