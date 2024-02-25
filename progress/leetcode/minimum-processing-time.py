class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        j=0
        res=0
        for i in processorTime:
            while (j+1)%4!=0:
                res=max(res,(i+tasks[j]))
                j+=1
            res=max(res,(i+tasks[j]))
            j+=1
        return res

