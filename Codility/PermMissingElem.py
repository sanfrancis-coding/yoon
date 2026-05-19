# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    return ((N+1)*(N+2)) // 2 - sum(A)