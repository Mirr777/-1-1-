"""
최솟값 찾기 1

N개의 수 A1, A2, An 과 L 이 주어진다. A(i-L+1) ~ Ai 중 최솟값을 D라고 할 때 
D에 저장된 수를 출력하는 프로그램을 작성하시오.

입력
1번째 줄에 N과 L ,2번째 줄에 N개의 수가 주어진다.

출력
1번째 줄에 Di를 공백으로 구분해 순서대로 출력한다.

예제 입력 1

12 3
1 5 2 3 6 2 3 7 3 5 2 6

예제 출력 1

1 1 1 2 2 2 2 2 3 3 2 2


"""

"""
문제 분석하기
일정 범위 안에서 최솟값을 구하는 문제이므로 슬라이딩 윈도우와 정렬을 사용하면 될 것
같음. 윈도우의 크기는 문제에서 최솟값을 구하는 범위가 i-L+1 부터 i까지 이므로 L로
생각하면 됨. 최솟값을 찾기 위한 정렬은? 일반적으로 정렬은 O(nlong)의 시간 복잡도
를 가지므로 N과 L의 최대 범위가 5000000인 이 문제에서는 정렬을 사용할 수 없음.
다시 말해  O의 시간 복잡도로 해결해야 함. 하지만 슬라이딩 윈도우를 덱으로 구현
하여 정렬 효과를 볼 수 있음. 우선 덱의 구조를 이해해 봅시다.

1. 최소값 가능성 없는 데이터 삭제
2. window 크기 밖 데이터 삭제

"""

import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
mydeque = deque();
now = list(map(int, input().split()))

for i in range(N):
    #아이디어1. 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L: # 윈도우 범위가 벗어나면
        mydeque.popleft()
    print(mydeque[0][0], end=" ")