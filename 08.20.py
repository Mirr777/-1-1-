"""
에지의 가중치가 10 이하인 자연수의 방향 그래프가 있다.
이 그래프의 시작접에서 다른 모든 노드로의 최단 경로를 구하시오.

다익스트라 알고리즘을 구현할 수 있는가?

예제 입력 1
5, 6 노드의 개수와 에지의 개수
1 출발 노드
5 1 1  에지 정보
1 2 2
1 3 3
2 3 4 
2 4 5
3 4 6

시작점과 다른 노드와 관련된 최단 거리를 구하는 문제
다익스트라 - 에지가 무조건 양수이므로
벨만포드

손으로 풀어보기
인접 리스트에 노드를 저장하고 거리 리스트를 초기화 함. 거리 리스트는
앞에서 설명했듯이 출발 노드는 0 , 나머지는 무한으로 초기화 됨.

최초 시작점을 우선순위 큐에 삽입하고, 다음 과정에 따라 다익스트라 알고리즘
을 수행합니다.

다익스트라 알고리즘 수행 과정
1. 거리 리스트에서 아직 방문하지 않는 노드 중 현재 값이 가장 작은 노드를 선택
즉, 우선순위 큐에서 데이터를 뽑아온다.

2. 해당 노드에 연결된 노드들의 최단 거릿값을 다음 공식을 이용해 업데이트
[연결 노드 거리 리스트 값]보다 [선택 노드의 거리 리스트 값 + 에지 가중치]가
더 작은 경우 업데이트 수행
업데이트가 수행되는 경우 연결 노드를 우선순위 큐에 삽입



"""

import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize]*(V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

q.put((0, K))
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")

