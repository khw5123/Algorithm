import sys
input = sys.stdin.readline

def merge(l, r):
    m = (l+r)//2
    i, j = l, m+1
    tmp = []
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i > m:
        while j <= r:
            tmp.append(arr[j])
            j += 1
    else:
        while i <= m:
            tmp.append(arr[i])
            i += 1
    for idx in range(l, r+1):
        arr[idx] = tmp[idx-l]

def partition(l, r):
    if l < r:
        m = (l+r)//2
        partition(l, m)
        partition(m+1, r)
        merge(l, r)

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
partition(0, n-1)
for v in arr:
    print(v)