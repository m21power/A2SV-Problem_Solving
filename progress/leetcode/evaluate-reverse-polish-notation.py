class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper=["+", "-", "*", "/"]
        for tok in tokens:
            if tok not in oper:
                stack.append(tok)
            else:
                a=stack.pop()
                b=stack.pop()
                if tok=='+':
                    stack.append(int(a)+int(b))
                elif tok =='-':
                    stack.append(int(b)-int(a))
                elif tok =='*':
                    stack.append(int(a)*int(b))
                elif tok =='/':
                    stack.append(int(b)/int(a))
        return int(stack[-1])


        