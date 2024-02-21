class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list(map(str,s))
        n=[]
        for let in s:
            if let.isalpha():
                n.append(let.lower())
            if let.isnumeric():
                n.append(let)
        a=list(reversed(n))
        if n == a:
            return True
        else:
            return False