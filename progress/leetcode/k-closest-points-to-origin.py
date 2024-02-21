class Solution:
    def distance(self,points):
        return ((points[0])**2+(points[1])**2)**0.5
    def kClosest(self, points ,k: int) :
        dic={}
        lis=[]
        stack=[]
        for pt in points:
            if self.distance(pt) in dic:
                stack.append(pt)
            else:
                dic[self.distance(pt)]=pt
        di=sorted(dic)
        j=0
        for i in di:
            j+=1
            lis.append(dic[i])
            for m in stack:
                if self.distance(m)==i:
                    lis.append(m)
                    j+=1
            if j==k:
                break
        return lis