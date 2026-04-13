from collections import Counter

N = int(input())
arr = list(map(int, input().split()))

F = Counter(arr)
stack = []

answer = [-1]*N

for i in range(N):
    while stack and F[arr[stack[-1]]] < F[arr[i]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
