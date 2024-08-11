# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        dic={'X++':'1','++X':'1','X--':'-1','--X':'-1'}
        for i in operations:
            x+=int(dic[i])
        return x
        