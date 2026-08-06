"""
크기가 N인 수열 A = A1, A2 ... An이 있다. 수열의 각 원소 Ai에 
관련한 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 
있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수를 의미한다.
이러한 수가 없을 떄 오큰수는 -1이다. 예를 들어 A = [3, 5, 2, 7]
일 때 NGE(1) = 5, NGE(2) = 7 NGE(2) = 7, NGE(3) = 7,
NGE(4) = -1이다. A = [9, 5, 4, 8]일 경우에는 NGE(1) = -1,
NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력
1번째 줄에 수열 A의 크기 N(1 <= N <= 1,000,000), 2번째 
줄에 수열 A의 원소 A1,A2, AN이 주어진다.


예제 입력 
4
3 5 2 7

예제 출력

5 7 7 -1


"""

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""
for i in range(n):
    result += str(ans[i]) + " "

print(result)