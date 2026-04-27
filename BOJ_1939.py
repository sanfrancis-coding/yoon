from collections import deque

N, M = map(int, input().split())   # N: 섬의 개수, M: 다리의 개수 입력
graph = [[] for _ in range(N + 1)] # 1번 섬부터 N번 섬까지 쓰기 위해 인접 리스트 생성

min_w = 10**9   # 입력되는 다리 중 최소 중량 제한을 저장할 변수 (아주 큰 값으로 시작)
max_w = 1       # 입력되는 다리 중 최대 중량 제한을 저장할 변수

for _ in range(M):   # M개의 다리 정보 입력
    A, B, C = map(int, input().split())   # A섬과 B섬을 연결하는 다리, 중량 제한은 C
    graph[A].append((B, C))   # A에서 B로 갈 수 있고, 그 다리의 중량 제한은 C
    graph[B].append((A, C))   # B에서 A로도 갈 수 있으므로 양방향으로 저장
    min_w = min(min_w, C)     # 전체 다리 중 최소 중량 제한 갱신
    max_w = max(max_w, C)     # 전체 다리 중 최대 중량 제한 갱신

start, end = map(int, input().split())   # 출발 섬과 도착 섬 입력

def can_move(weight):   # weight 무게의 물건을 start에서 end까지 옮길 수 있는지 확인하는 함수
    visited = [False] * (N + 1)   # BFS 방문 체크 배열
    queue = deque([start])        # BFS 시작점은 start
    visited[start] = True         # 시작 섬 방문 처리

    while queue:                  # 탐색할 노드가 남아 있는 동안 반복
        now = queue.popleft()     # 현재 섬 하나 꺼내기

        if now == end:            # 도착 섬에 도달했다면
            return True           # weight 무게를 옮길 수 있다는 뜻

        for nxt, limit in graph[now]:   # 현재 섬과 연결된 다음 섬들 확인
            if not visited[nxt] and limit >= weight:  # 아직 방문 안 했고, 다리가 weight를 버틸 수 있으면
                visited[nxt] = True     # 방문 처리
                queue.append(nxt)       # 다음 탐색 대상으로 큐에 넣기

    return False   # BFS가 끝날 때까지 end에 도달 못했으면 weight는 옮길 수 없음

left, right = min_w, max_w   # 이분 탐색 범위: 가능한 최소 중량 ~ 가능한 최대 중량
answer = min_w               # 정답 후보를 일단 최소 중량으로 시작

while left <= right:         # 이분 탐색 수행
    mid = (left + right) // 2   # 현재 시험할 중량

    if can_move(mid):        # mid 무게를 옮길 수 있으면
        answer = mid         # 일단 정답 후보로 저장
        left = mid + 1       # 더 무거운 것도 가능한지 확인하기 위해 범위를 오른쪽으로 이동
    else:                    # mid 무게를 옮길 수 없으면
        right = mid - 1      # 무게를 줄여야 하므로 범위를 왼쪽으로 이동

print(answer)   # 최대로 옮길 수 있는 중량 출력