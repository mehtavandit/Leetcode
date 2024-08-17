class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def dfs(r ,c):
            if r<0 or r>= len(image) or c<0 or c>= len(image[0]) or image[r][c] != start_color:
                return

            image[r][c] = color

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r, c-1)
            dfs(r, c+1)


        dfs(sr, sc)

        return image