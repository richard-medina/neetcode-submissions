class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = [int(tokens[0]), int(tokens[1])]

        
        for i in range(2, len(tokens)):
            if tokens[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]

               






