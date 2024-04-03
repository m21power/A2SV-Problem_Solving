class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row,col = len(image),len(image[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]] 
        val,visited = image[sr][sc],set()

        def dfs(r,c):
            if (r == row or c == col  
               or min(r,c) < 0 or
                (r,c) in visited or image[r][c] != val) :
               return
            if image[r][c] == val:
                image[r][c] = color
        
            visited.add((r,c))
            for dr,dc in direction:
                nr, nc = dr + r,dc + c
                dfs(nr,nc)
            

        dfs(sr,sc)
        return image


        