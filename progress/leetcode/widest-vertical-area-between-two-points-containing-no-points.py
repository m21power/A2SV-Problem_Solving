class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        i=1
        """while i<len(points):
            j=i
            while j>0 and points[j][0] < points[j-1][0]:
                points[j],points[j-1] =points[j-1],points[j]
                j-=1
            i+=1"""
        points.sort()
        m=points[1][0]-points[0][0]
        i=1
        while i<len(points)-1:
            m=max(m,points[i+1][0]-points[i][0])
            i+=1
        return m


        