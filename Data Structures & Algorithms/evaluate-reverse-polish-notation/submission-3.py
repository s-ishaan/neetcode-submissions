class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        soln = int(tokens[0])
        stack.append(soln)
        operators = ['+', '/', '*', '-']
        for i in range(1, len(tokens)):
            char = tokens[i]
            if char not in operators:
                stack.append(char)
            elif char in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if char == '+':
                    soln = num1 + num2
                if char == '-':
                    soln = num2-num1
                if char == '*':
                    soln = num1 * num2
                if char == '/':
                    soln = int(num2/num1)
                stack.append(soln)
            
        return soln
                    