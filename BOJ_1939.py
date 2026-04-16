# 이분탐색

from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

min_w = 10**9
max_w = 1

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    min_w = min(min_w, C)
    max_w = max(max_w, C)

start, end = map(int, input().split())

def can_move(weight):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        if now == end:
            return True
        for nxt, limit in graph[now]:
            if not visited[nxt] and limit >= weight:
                visited[nxt] = True
                queue.append(nxt)
    return False

left, right = min_w, max_w
answer = min_w
while left <= right:
    mid = (left + right) // 2
    if can_move(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)