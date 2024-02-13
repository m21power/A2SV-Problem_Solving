class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        LR=len(matrix[0])
        LC=len(matrix)
        i=0
        
        lis=[]
        while i<LR:
            j=0
            temp=[]
            while j<LC:
                temp.append(matrix[j][i])
                j+=1
            lis.append(temp)
            i+=1

        return lis
