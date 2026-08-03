"""
N개의 수 가 주어졌을 때, 연속된 부분의 합이 M으로 나누어떨어지는 
구간의 개수를  구하는 프로그램을 작성하시오. 즉, N개의  수의 합이
M으로 나누어떨어지는 (i,j) 쌍의 개수를 구하시오.

1번째 줄에 N과 M, 2번째 줄에 N개의 수가 주어진다.

예제 입력 1
5 3
1 2 3 1 2

예제 출력 1
7

"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m

    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)