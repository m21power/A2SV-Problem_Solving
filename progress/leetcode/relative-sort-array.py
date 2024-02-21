class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        for i in arr2:
            for n in range(arr1.count(i)):
                output.append(i)
        arr1.sort()
        for i in arr1:
            if i not in arr2:
                output.append(i)
        return output
        
        