from collections import deque

def min_flips_to_connect_islands(grid):
    n = len(grid)
    m = len(grid[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False]*m for _ in range(n)]
    island1 = []
    island2 = []

    # DFS to collect island cells
    def dfs(x, y, island):
        stack = [(x, y)]
        visited[x][y] = True

        while stack:
            cx, cy = stack.pop()
            island.append((cx, cy))

            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

    # Find two islands
    islands_found = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                if islands_found == 0:
                    dfs(i, j, island1)
                else:
                    dfs(i, j, island2)
                islands_found += 1

    # BFS from edge of island1
    q = deque()
    used = [[False]*m for _ in range(n)]
    level = [[0]*m for _ in range(n)]

    for x, y in island1:
        # check if edge cell
        edge = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0:
                    edge = True

        if edge:
            q.append((x, y))
            used[x][y] = True
            level[x][y] = 1

    # BFS expansion
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not used[nx][ny]:
                used[nx][ny] = True
                level[nx][ny] = level[x][y] + 1
                q.append((nx, ny))

    # Find closest cell from island2
    ans = float('inf')
    for x, y in island2:
        ans = min(ans, level[x][y])

    return ans - 1
    
    

grid = [
    [1,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,1]
]

print(min_flips_to_connect_islands(grid))