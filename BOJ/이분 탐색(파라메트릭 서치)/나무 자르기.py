import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))
left, right = 0, 1000000000
while left+1 < right:
    mid = (left+right)//2
    length = 0
    for h in height:
        if h > mid:
            length += (h-mid)
    if length >= m:
        left = mid
    else:
        right = mid
print(left)