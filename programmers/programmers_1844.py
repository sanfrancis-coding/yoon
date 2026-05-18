from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return visited[n-1][m-1]