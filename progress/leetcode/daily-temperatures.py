class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        stack=[]
        output=[0]*len(temp)
        for i,n in enumerate(temp):
            while stack and temp[stack[-1]]<n:
                output[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return output