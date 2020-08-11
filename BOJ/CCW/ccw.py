def ccw(x1, y1, x2, y2, x3, y3):
    op = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    if op > 0: # 반시계 방향
        return 1
    elif op < 0: # 시계 방향
        return -1
    else: # 일직선
        return 0

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(ccw(x1, y1, x2, y2, x3, y3))