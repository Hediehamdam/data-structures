"""
File Name: number_of_islands.py
Description: Counts the number of islands in a 2D matrix using DFS.
Data Structure/Algorithm: 2D Matrix, Depth First Search
Operations: dfs, count_islands
Use Case: Grid processing, graph traversal, practicing DFS
"""

def dfs(matrix, visited, i, j, rows, cols):
    if i<0 or i>=rows or j<0 or j>=cols or matrix[i][j] == 0 or visited[i][j]:
        return
    visited[i][j] = True
    # explore all 4 directions
    dfs(matrix, visited, i+1, j, rows, cols)
    dfs(matrix, visited, i-1, j, rows, cols)
    dfs(matrix, visited, i, j+1, rows, cols)
    dfs(matrix, visited, i, j-1, rows, cols)

def count_islands(matrix):
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix, visited, i, j, rows, cols)
                count += 1
    return count

if __name__ == "__main__":
    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]
    ]
    print("Number of islands:", count_islands(grid))
