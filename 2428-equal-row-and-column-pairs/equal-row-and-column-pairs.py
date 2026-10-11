class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_map = defaultdict(int)
        col_map = defaultdict(int)
        count = 0

        for row in grid:
            row_map[tuple(row)] += 1
        
        j = 0

        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                
                col.append(grid[j][i])

            col_map[tuple(col)] += 1
        
        for key in row_map:
            if key in col_map:
                count += row_map[key] * col_map[key]
        
        return count