import sys
input = sys.stdin.readline

n, arr = int(input()), sorted(list(map(int, input().split())))
m, target = int(input()), list(map(int, input().split()))
for num in target:
    answer = 0
    left, right = 0, n-1
    mid = (left+right)//2
    while left <= right:
        if arr[mid] == num:
            answer = 1
            break
        if arr[mid] > num:
            right = mid-1
        else:
            left = mid+1
        mid = (left+right)//2
    print(answer, end=' ')
print()