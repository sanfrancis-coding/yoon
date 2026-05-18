from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [input().strip() for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

visited = [[bytearray(K + 1) for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, 0))   # x, y, broken
    visited[0][0][0] = 1
    dist = 1

    g = graph
    v = visited
    n = N
    m = M
    k = K
    dxs = dx
    dys = dy

    while q:
        for _ in range(len(q)):
            x, y, broken = q.popleft()

            if x == n - 1 and y == m - 1:
                return dist

            for i in range(4):
                nx = x + dxs[i]
                ny = y + dys[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                cell = g[nx][ny]

                if cell == '0':
                    if not v[nx][ny][broken]:
                        v[nx][ny][broken] = 1
                        q.append((nx, ny, broken))
                else:
                    nb = broken + 1
                    if nb <= k and not v[nx][ny][nb]:
                        v[nx][ny][nb] = 1
                        q.append((nx, ny, nb))

        dist += 1

    return -1

print(bfs())