class Solution:
    def smallestNumber(self, num: int) -> int:
        lis=0
        if num>0:
            num=str(num)
            lis=list(map(int,num))
            lis.sort()
            print(lis)
            if lis[0]==0:
                for i,n in enumerate(lis):
                    if n!=0:
                        lis[0],lis[i]=n,lis[0]
                        break
            lis=list(map(str,lis))
            print(lis)
            return int(''.join(lis))
        elif num<0:
            num=-1*num
            num=str(num)
            lis=list(map(int,num))
            lis.sort(reverse=True)
            print(lis)
            if lis[0]==0:
                for i,n in enumerate(lis):
                    if n!=0:
                        lis[0],lis[i]=n,lis[0]
                        break
            lis=list(map(str,lis))
            print(lis)
            return -int(''.join(lis))
        else:
            return 0