class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':   toadd = a+b
                elif token == '-': toadd = a-b
                elif token == '*': toadd = a*b
                else:              toadd = int(a/b)
                
                stack.append(toadd)
        
        return stack.pop()
        