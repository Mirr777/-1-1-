"""
ATM 인출 시간 계산하기

ATM이 한 대 밖에 없다. 지금 ATM 앞에 N명의 사람들이 줄을 서
있다. 사람은 1번에서 N번까지 번호가 있으며, i번 사람이 돈을
인출할 때 걸리는 시간은 pi분이다.
사람들이 줄을 서는 순서에 따라서 돈을 인출하는데 필요한 시간의
합이 달라진다.
예를 들어 총 5명이 있고, p1 = 3, p2 = 1, p3 = 4, p4 = 3,
p5 =2일 때를 생각해보자. [1,2,3,4,5] 순서로 줄을 선다면
1번 살마은 3분만에 돈을 뽑을 수 있다. 2번 사람은 1번 사람이
돈을 뽑을 때까지 기다려야 하므로 3+1= 4분이 걸린다.

예제 입력
5
3 1 4 3 2

출력 입력

32

"""


"""
# 직접 푼 코드
n = list(map(int, input().split()))
new_n = sorted(n)[::-1]
a= 1
answer = 0
for i in new_n:
    answer += i * a
    a += 1
print(answer)
"""

N = int(input())
A = list(map(int, input().split()))
S = [0]*N


for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0

    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value


S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0, N):
    sum += S[i]

print(sum)


