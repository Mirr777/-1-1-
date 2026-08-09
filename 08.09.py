"""
버블 정렬은 서로 인접해 있는 두 수를 바꾸면서 정렬하는 방법이다.
예를 들어 수열이 3, 2, 1이었다고 가정하면 이 때는 인접해 있는
3, 2가 바뀌어야 하므로 2,3,1이 된다. 그 다음은 3,1이 바뀌어야
하므로 3,1이 된다. 그 다음은 3,1이 바뀌어야 하므로 2,1,3이
된다. 그 다음에는 2,1이 바뀌어야 하므로 1,2,3이 된다. 그러면
더 이상 바꿀 수 없으므로 정렬이 완료된다.
N개의 수로 이뤄진 수열이 있다. 이 수열로 버블 정렬을 수행할 때
swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오

예제 입력 1
8
3 2 8 1 7 4 5 6

예제 출력 

11


"""

import sys
input = sys.stdin.readline
result = 0



def merge_sort(s, e):
    global result
    if e-s < 1: return
    m = int(s+(e-s)/2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <=e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
tmp = [0] * int(N+1)
merge_sort(1,N)
print(result)