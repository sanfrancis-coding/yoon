def solution(A):
    total = sum(A)
    min_diff = float('inf')
    left_sum = 0
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)
    return min_diff