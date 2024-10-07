class Solution(object):
    def floodFill(self, image, sr, sc, color):
        starting = image[sr][sc] 
        self.dfs(image,sr,sc,color,starting)
        return image  
        
    def dfs(self,image,sr,sc,color,starting):
        #basecase 
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] == color or image[sr][sc] != starting:
            return
        
        #otherwise
        image[sr][sc] = color
        self.dfs(image,sr+1,sc,color,starting)
        self.dfs(image,sr-1,sc,color,starting)
        self.dfs(image,sr,sc+1,color,starting)
        self.dfs(image,sr,sc-1,color,starting)
            
 
    
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        