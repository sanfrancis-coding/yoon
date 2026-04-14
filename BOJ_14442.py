from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [input().strip() for _ in range(N)]

# bool 3차원 리스트보다 bytearray가 더 가볍다
visited = [[bytearray(K + 1) for _ in range(M)] for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def bfs():
    queue = deque()
    queue.append((0, 0, 0))   # x, y, state
    visited[0][0][0] = 1

    dist = 1

    while queue:
        for _ in range(len(queue)):
            x, y, state = queue.popleft()

            if x == N - 1 and y == M - 1:
                return dist

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                # case 1 : 빈칸
                if graph[nx][ny] == '0':
                    if not visited[nx][ny][state]:
                        visited[nx][ny][state] = 1
                        queue.append((nx, ny, state))

                # case 2 : 벽 부수기
                elif state < K:
                    if not visited[nx][ny][state + 1]:
                        visited[nx][ny][state + 1] = 1
                        queue.append((nx, ny, state + 1))

        dist += 1

    return -1

print(bfs())