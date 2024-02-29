class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=['/']
        path = path.split('/')

        for p in path:
            if p =='.' or p=='/' or p=='':
                pass
            elif p=='..':
                while stack:
                    stack.pop()
                    if stack and stack[-1]=='/':
                        break
            else:
                if not stack:
                    stack.append('/')
                stack.append(p)
                stack.append('/')
        if stack and stack[-1]=='/':
            stack.pop()
        if not stack:
            stack.append('/')
        return ''.join(stack)
