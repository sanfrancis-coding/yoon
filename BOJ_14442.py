# state = 지금까지 부순 벽의 개수

from collections import deque
N,M,K = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)] # state = {(0,1,2,...,k)} 이므로 k+1 사용
dist = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

dx= [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append((0,0,0)) # x, y, state
    visited[0][0][0] = True
    dist[0][0][0] = 1

    while queue:
        x, y, state = queue.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y][state]
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # case 1 : 빈칸일 경우
            if graph[nx][ny] == 0 and not visited[nx][ny][state]:
                visited[nx][ny][state] = True
                dist[nx][ny][state] = dist[x][y][state] + 1
                queue.append((nx,ny,state))
            # case 2: 벽일 경우
            if graph[nx][ny] == 1 and state <K and not visited[nx][ny][state+1]:
                visited[nx][ny][state+1] = True
                dist[nx][ny][state+1] = dist[x][y][state] + 1
                queue.append((nx, ny, state+1))
    return -1
print(bfs())