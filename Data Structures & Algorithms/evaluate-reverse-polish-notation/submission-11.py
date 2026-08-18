class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '/', '-', '*'}
        soln = None
        for char in tokens:
            if char in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                if char == '+':
                    soln = num1 + num2
                elif char == '*':
                    soln = num1 * num2
                elif char == '-':
                    soln = num2 - num1
                elif char == '/':
                    soln = int(num2/num1)
                stack.append(soln)
            else:
                stack.append(int(char))

        return stack[-1]