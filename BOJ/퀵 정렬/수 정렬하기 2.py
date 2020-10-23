import sys
input = sys.stdin.readline

def quickSort(l, r):
    if l >= r:
        return
    pivot = arr[(l+r)//2]
    left, right = l, r
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left +1, right - 1
    quickSort(l, right)
    quickSort(left, r)

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
quickSort(0, n-1)
for v in arr:
    print(v)