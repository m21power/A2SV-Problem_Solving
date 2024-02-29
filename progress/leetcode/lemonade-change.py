class Solution:
    def lemonadeChange(self, bills) :
        five=0
        ten=0
        twenty=0
        for n in bills:
            if n==5:
                five+=1
            elif n==10:
                if five<1:
                    return False
                five-=1
                ten+=1
            else: # when 20 comes
                if five>=1 and ten>=1:
                    five-=1
                    ten-=1
                    
                elif five>=3:
                    five-=3
                else:
                    return False
                twenty+=1
        return True

