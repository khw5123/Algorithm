import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))
left, right = 0, 2**31
answer = 0
while left+1 < right:
    mid = (left+right)//2
    length = 0
    for l in lan:
        length += (l//mid)
    if length >= n:
        left = mid
        answer = max(answer, mid)
    else:
        right = mid
print(left)