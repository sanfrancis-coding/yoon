from collections import deque

def is_valid(place):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue
            # P일때만 방문을 탐색한다.
            visited = [[False]*5 for _ in range(5)]
            queue = deque()
            queue.append((i,j,0))
            visited[i][j] = True

            while queue:
                x,y,dist = queue.popleft()
                if dist >= 2:
                    continue
                # 맨해튼 거리가 2 이하일 때만 탐지
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]

                    if not (0<=nx<5 and 0<=ny<5):
                        continue
                    if visited[nx][ny]:
                        continue
                    if place[nx][ny] == 'X':
                        continue
                    if place[nx][ny] == 'P':
                        return False
                    visited[nx][ny] = True
                    queue.append((nx,ny,dist+1))
    return True

def solution(places):
    return [1 if is_valid(place) else 0 for place in places]
