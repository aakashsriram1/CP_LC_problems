class Solution(object):
    def floodFill(self, image, sr, sc, color):
        R = len(image)
        C = len(image[0])
        newColor = image[sr][sc]
        if newColor == color:
            return image 
        def dfs(r,c): 
            if image[r][c] == newColor: 
                image[r][c] = color
                if r >= 1: 
                    dfs(r-1,c)
                if r+1 < R: 
                    dfs(r+1,c)
                if c >= 1: 
                    dfs(r,c-1)
                if c+1 < C: 
                    dfs(r,c+1)
        dfs(sr,sc)
        return image
        

        
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        