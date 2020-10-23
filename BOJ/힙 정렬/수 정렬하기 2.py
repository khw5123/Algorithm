import sys
input = sys.stdin.readline

def heapify(i, n):
    left, right = i*2, i*2 + 1
    idx = i
    if left <= n and arr[idx] < arr[left]:
        idx = left
    if right <= n and arr[idx] < arr[right]:
        idx = right
    if idx != i:
        arr[i], arr[idx] = arr[idx], arr[i]
        heapify(idx, n)

def heapSort():
    for i in range(n//2, 0, -1): # 리프 노드 제외
        heapify(i, n)
    for i in range(n, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(1, i-1)

n = int(input())
arr = [0]*(n+1)
for i in range(1, n+1):
    arr[i] = int(input())
heapSort()
for i in range(1, n+1):
    print(arr[i])