import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    op = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    if op > 0: # 반시계 방향
        return 1
    elif op < 0: # 시계 방향
        return -1
    else: # 평행
        return 0

def hasIntersectionPoint(x11, y11, x12, y12, x21, y21, x22, y22):
    ab = ccw(x11, y11, x12, y12, x21, y21)*ccw(x11, y11, x12, y12, x22, y22)
    cd = ccw(x21, y21, x22, y22, x11, y11)*ccw(x21, y21, x22, y22, x12, y12)
    if ab == 0 and cd == 0:
        a, b = ((x12, y12), (x11, y11)) if (x11, y11) > (x12, y12) else ((x11, y11), (x12, y12))
        c, d = ((x22, y22), (x21, y21)) if (x21, y21) > (x22, y22) else ((x21, y21), (x22, y22))
        if c <= b and a <= d:
            return True
        else:
            return False
    if ab <= 0 and cd <= 0:
        return True
    else:
        return False

def find(a):
    if a == li[a]:
        return a
    li[a] = find(li[a])
    return li[a]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if count[b] > count[a]:
        a, b = b, a
    li[b] = a
    count[a] += count[b]
    count[b] = 0

n = int(input())
coords, li, count = [], [i for i in range(n)], [1]*n
for _ in range(n):
    coords.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        if hasIntersectionPoint(coords[i][0], coords[i][1], coords[i][2], coords[i][3], coords[j][0], coords[j][1], coords[j][2], coords[j][3]):
            union(i, j)
print(len(count) - count.count(0))
print(max(count))