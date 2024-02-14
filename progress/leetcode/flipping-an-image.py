class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        i=0
        while i<n:
            image[i].reverse()
            i+=1
        for i in image:
            j=0
            while j<n:
                if i[j]==0:
                    i[j]=1
                else:
                    i[j]=0
                j+=1
        return image
        
