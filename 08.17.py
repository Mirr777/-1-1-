import math

def solution(n):
    answer = 0
    for i in range(n//2 + 1):
        answer += math.comb(n-i,i)
    return answer % 1234567