import sys
input = sys.stdin.readline

n, c = map(int, input().split())
coords = sorted([int(input()) for _ in range(n)])
left, right = 1, coords[-1]-coords[0]
answer = 0
while left <= right:
    mid = (left+right)//2
    start, count = coords[0], 1
    for i in range(1, n):
        if coords[i]-start >= mid:
            start, count = coords[i], count+1
    if count >= c:
        left = mid+1
        answer = mid
    else:
        right = mid-1
print(answer)