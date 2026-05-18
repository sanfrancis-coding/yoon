# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    started = False

    for bit in binary:
        if bit == '1':
            if started:
                max_gap = max(max_gap, current_gap) # 닫는 1인 경우
            started = True
            current_gap = 0
        else:
            if started:
                current_gap+=1
        
    return max_gap